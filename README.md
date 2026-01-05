# Claude Code Self-Learning Skills - Reflect System 🧠

> *"Correct once, never again"* - Self-learning skills that improve from your corrections

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude-Code-purple)](https://claude.ai/code)

---

## 🎯 What is this?

**Reflect** is a self-learning system for Claude Code that enables skills to improve based on your corrections. Instead of repeating mistakes, Claude **remembers** your preferences and never makes the same error twice.

### The Problem

```
Session 1: Claude uses pip
You:      "No, use uv instead"
Claude:   "Ok, using uv"

Session 2: Claude uses pip again 😞
You:      "I told you to use uv!"
```

### The Solution

```
Session 1: Claude uses pip
You:      "No, use uv instead"
          → /reflect → Skill learns ✅

Session 2: Claude uses uv ✨
Session 3: Claude uses uv ✨
Forever:  Claude uses uv ✨
```

---

## 🚀 Quick Start

### Installation

```bash
# Copy to your Claude Code skills directory
cp -r reflect ~/.claude/skills/
cp -r python-project-creator ~/.claude/skills/

# Check status
/reflect-status
```

### Basic Usage

1. **Work with Claude** - Let it make a mistake
2. **Correct it** - "No, use X instead of Y"
3. **Run reflection** - `/reflect`
4. **Review changes** - Approve with `A`
5. **Done!** - Claude learned permanently

### Commands

| Command | Action |
|---------|--------|
| `/reflect` | Analyze current session manually |
| `/reflect-on` | Enable auto-reflection at session end |
| `/reflect-off` | Disable auto-reflection |
| `/reflect-status` | Show current configuration |

---

## 📦 What's Included

### 🧠 Reflect System

The core learning engine with:

- ✅ Pattern detection (HIGH/MEDIUM/LOW confidence)
- ✅ Safe skill updates with backups
- ✅ Git integration for version control
- ✅ Interactive review flow
- ✅ Auto-reflection via hooks

**📖 [Complete User Guide](reflect/USER_GUIDE.md)**

### 🐍 Python Project Creator (Demo)

Example skill that demonstrates learning:

**Initial state:** Uses `pip` and `unittest`

**After corrections:**
1. ✅ Learned: Use `uv` instead of `pip`
2. ✅ Learned: Always `pytest`, never `unittest`

**Result:** Now always suggests `uv` and `pytest`!

---

## 🎓 How It Works

### Three Confidence Levels

#### 🔴 HIGH - Corrections
```
"No, use X instead of Y"
"Never do X"
"Always check Y"
```
→ Creates **Critical Corrections** section

#### 🟡 MEDIUM - Approvals
```
"Yes, perfect!"
"That works well"
"Exactly right"
```
→ Adds to **Best Practices**

#### 🟢 LOW - Observations
```
"Have you considered...?"
"What about...?"
```
→ Notes in **Considerations**

### Safe Application

Every change includes:
- ✅ Timestamped backup
- ✅ YAML validation
- ✅ User approval (manual mode)
- ✅ Automatic rollback on errors
- ✅ Git commit with description

---

## 📖 Example Learning Journey

### Step 1: Initial Mistake

Claude uses `pip install`:
```bash
pip install fastapi
pip freeze > requirements.txt
```

### Step 2: Your Correction

> "No, use uv instead of pip! It's faster and modern."

### Step 3: Reflection Detects

```
Signal detected:
- Type: HIGH confidence correction
- Pattern: "use X instead of Y"
- Old: pip
- New: uv
```

### Step 4: Skill Updated

```diff
+## Critical Corrections
+
+**Use 'uv' instead of 'pip'**
+- ✗ Don't: pip install
+- ✓ Do: uv pip install
```

### Step 5: Forever Learned

Next session, Claude automatically:
```bash
uv pip install fastapi
uv pip freeze > requirements.txt
```

**No reminder needed!** ✨

---

## 🛠️ Configuration

### Manual Mode (Recommended for beginners)

```bash
/reflect-status  # Should show "Disabled"
```

Run `/reflect` after sessions with corrections.

### Auto Mode (For continuous learning)

```bash
/reflect-on
```

Runs automatically at session end via Stop hook.

### Hook Setup

Already configured if you copied the skills! Check:

```bash
cat ~/.claude/settings.local.json | grep -A 5 hooks
```

Should show hook for `reflect/scripts/hook-stop.sh`.

---

## 🎯 Best Practices

### ✅ Do

- Start with manual `/reflect` to learn the system
- Be specific: "Use X instead of Y"
- Review diffs before approving
- Check git history regularly
- Enable auto-mode after you trust it

### ❌ Don't

- Be vague: "That's wrong" (won't detect)
- Contradict yourself: Creates conflicts
- Skip reviews: Always check changes
- Delete backups: They save you!

---

## 📚 Documentation

- **[User Guide](reflect/USER_GUIDE.md)** - Complete walkthrough with examples
- **[README](reflect/README.md)** - Quick reference
- **[Signal Patterns](reflect/references/signal-patterns.md)** - Detection patterns

---

## 🧪 Try It Yourself

### Demo Workflow

```bash
# 1. Ask Claude to create a Python project
"Create a Python FastAPI project"

# 2. Claude uses pip (as currently documented)
# 3. Correct it:
"No, always use uv instead of pip!"

# 4. Run reflection:
/reflect

# 5. Review and approve the changes

# 6. Next time, Claude automatically uses uv!
```

---

## 🔍 What Makes This Special?

**Unlike other AI coding tools:**

❌ Most tools: Forget everything each session
✅ Reflect: Builds permanent knowledge

❌ Most tools: Repeat same mistakes
✅ Reflect: Learn from corrections

❌ Most tools: No version control
✅ Reflect: Full git history

❌ Most tools: Black box learning
✅ Reflect: Transparent, reviewable changes

---

## 🛡️ Safety

- **Backups**: Every change backed up with timestamp
- **Validation**: YAML frontmatter validated
- **Rollback**: Auto-rollback on errors
- **Git**: Full version control
- **Approval**: No surprises (manual mode)

---

## 📊 System Requirements

- Claude Code (CLI)
- Python 3.8+
- Git
- macOS/Linux (Windows untested)

---

## 🤝 Contributing

Create your own learning skills! Follow the python-project-creator example:

1. Create skill with standard structure
2. Use it and provide corrections
3. Run `/reflect`
4. Watch it improve!

---

## 📝 License

MIT License - Use freely!

---

## 🙏 Credits

Inspired by the "correct once, never again" philosophy.

Built for Claude Code users who want AI that actually remembers.

---

## 🔗 Links

- **Claude Code**: https://claude.ai/code
- **Issues**: https://github.com/haddock-development/claude-reflect-system/issues

---

**Made with Claude Code 🤖**

*System learns, you benefit* ✨
