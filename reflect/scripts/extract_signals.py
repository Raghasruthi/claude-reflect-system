#!/usr/bin/env python3
"""
Extracts learning signals from conversation transcripts.
Identifies corrections, approvals, and patterns with confidence levels.
"""

import json
import re
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

# Correction patterns (HIGH confidence)
CORRECTION_PATTERNS = [
    r"(?i)no,?\s+don't\s+(?:do|use)\s+(.+?)[,.]?\s+(?:do|use)\s+(.+)",
    r"(?i)actually,?\s+(.+?)\s+(?:is|should be)\s+(.+)",
    r"(?i)instead\s+of\s+(.+?),?\s+(?:you\s+should|use|do)\s+(.+)",
    r"(?i)never\s+(?:do|use)\s+(.+)",
    r"(?i)always\s+(?:do|use|check for)\s+(.+)",
]

# Approval patterns (MEDIUM confidence)
APPROVAL_PATTERNS = [
    r"(?i)(?:yes,?\s+)?(?:that's\s+)?(?:perfect|great|exactly|correct)",
    r"(?i)works?\s+(?:perfectly|great|well)",
    r"(?i)(?:good|nice)\s+(?:job|work)",
]

# Question patterns (LOW confidence)
QUESTION_PATTERNS = [
    r"(?i)have\s+you\s+considered\s+(.+)",
    r"(?i)why\s+not\s+(?:try|use)\s+(.+)",
    r"(?i)what\s+about\s+(.+)",
]

def extract_signals(transcript_path: Optional[str] = None) -> Dict[str, List[Dict[str, Any]]]:
    """
    Parse transcript and extract learning signals.
    Returns dict of signals grouped by skill name.
    """
    if not transcript_path:
        # Get latest transcript from session env
        transcript_path = find_latest_transcript()

    if not transcript_path or not Path(transcript_path).exists():
        print(f"Warning: Transcript not found: {transcript_path}")
        return {}

    signals = []
    messages = load_transcript(transcript_path)

    # Track which skills were used
    skills_used = find_skill_invocations(messages)

    for i, msg in enumerate(messages):
        if msg.get('role') != 'user':
            continue

        content = str(msg.get('content', ''))
        context = messages[max(0, i-5):i+1]  # 5-message context

        # Check for corrections (HIGH)
        for pattern in CORRECTION_PATTERNS:
            if match := re.search(pattern, content):
                signals.append({
                    'confidence': 'HIGH',
                    'type': 'correction',
                    'content': content,
                    'context': context,
                    'skills': skills_used if skills_used else ['general'],
                    'match': match.groups() if match.groups() else (content,),
                    'description': extract_correction_description(content, match)
                })

        # Check for approvals (MEDIUM)
        prev_msg = messages[i-1] if i > 0 else None
        if prev_msg and prev_msg.get('role') == 'assistant':
            for pattern in APPROVAL_PATTERNS:
                if re.search(pattern, content):
                    signals.append({
                        'confidence': 'MEDIUM',
                        'type': 'approval',
                        'content': content,
                        'context': context,
                        'skills': skills_used if skills_used else ['general'],
                        'previous_approach': extract_approach(prev_msg),
                        'description': 'Approved approach'
                    })

        # Check for questions (LOW)
        for pattern in QUESTION_PATTERNS:
            if match := re.search(pattern, content):
                signals.append({
                    'confidence': 'LOW',
                    'type': 'question',
                    'content': content,
                    'context': context,
                    'skills': skills_used if skills_used else ['general'],
                    'suggestion': match.group(1) if match.groups() else content,
                    'description': f'Consider: {match.group(1) if match.groups() else content}'
                })

    return group_by_skill(signals)

def find_latest_transcript() -> Optional[str]:
    """Find the most recent transcript file"""
    try:
        # Check for TRANSCRIPT_PATH env variable first
        if os.getenv('TRANSCRIPT_PATH'):
            return os.getenv('TRANSCRIPT_PATH')

        # Try to find in session directory
        session_dir = Path(os.getenv('SESSION_DIR', Path.home() / '.claude' / 'session-env')).expanduser()
        if session_dir.exists():
            transcripts = list(session_dir.glob('*/transcript.jsonl'))
            if transcripts:
                return str(max(transcripts, key=lambda p: p.stat().st_mtime))
    except Exception as e:
        print(f"Error finding transcript: {e}")

    return None

def load_transcript(path: str) -> List[Dict[str, Any]]:
    """Load JSONL transcript into message list"""
    messages = []
    try:
        with open(path) as f:
            for line in f:
                if line.strip():
                    try:
                        msg = json.loads(line)
                        messages.append(msg)
                    except json.JSONDecodeError:
                        # Skip invalid lines
                        continue
    except Exception as e:
        print(f"Error loading transcript: {e}")

    return messages

def find_skill_invocations(messages: List[Dict[str, Any]]) -> List[str]:
    """Find which skills were invoked in conversation"""
    skills = set()
    for msg in messages:
        # Look for skill tool uses
        if 'tool_uses' in msg:
            for tool in msg.get('tool_uses', []):
                if tool.get('name') == 'Skill':
                    params = tool.get('parameters', {})
                    if 'skill' in params:
                        skills.add(params['skill'])

        # Look for /skill-name patterns
        content = str(msg.get('content', ''))
        if matches := re.findall(r'/([a-z][a-z0-9-]*)', content):
            skills.update(matches)

    return list(skills)

def extract_approach(message: Dict[str, Any]) -> str:
    """Extract the approach Claude took from assistant message"""
    content = str(message.get('content', ''))
    # Look for code blocks, tool uses, or key decisions
    return content[:500]  # First 500 chars as summary

def extract_correction_description(content: str, match) -> str:
    """Extract a human-readable description from correction pattern"""
    if match.groups():
        if len(match.groups()) == 2:
            return f"Use '{match.group(2)}' instead of '{match.group(1)}'"
        elif len(match.groups()) == 1:
            return f"Correction: {match.group(1)}"
    return "User provided correction"

def group_by_skill(signals: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Group signals by the skills they relate to"""
    grouped = {}
    for signal in signals:
        for skill in signal.get('skills', ['general']):
            if skill not in grouped:
                grouped[skill] = []
            grouped[skill].append(signal)
    return grouped

if __name__ == '__main__':
    # Test mode
    import sys
    if len(sys.argv) > 1:
        transcript = sys.argv[1]
    else:
        transcript = None

    signals = extract_signals(transcript)
    print(json.dumps(signals, indent=2))
