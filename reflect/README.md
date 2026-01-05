# Reflect - Self-Improving Skills System

> *"Correct once, never again"*

Ein intelligentes Lernsystem für Claude Code, das aus Ihren Korrekturen lernt und Skills automatisch verbessert.

---

## 🚀 Quick Start

```bash
# Status prüfen
/reflect-status

# Manuelle Analyse nach einer Session mit Korrekturen
/reflect

# Auto-Reflection aktivieren (optional)
/reflect-on
```

---

## 📖 Was ist Reflect?

Reflect analysiert Ihre Konversationen mit Claude und:

- ✅ **Erkennt Korrekturen** - Wenn Sie Claude korrigieren
- ✅ **Identifiziert Patterns** - Wenn Ansätze gut funktionieren
- ✅ **Aktualisiert Skills** - Basierend auf Ihrem Feedback
- ✅ **Versioniert Änderungen** - Mit Git-Integration

### Das Problem

```
Session 1: "Verwende uv statt pip"
Session 2: Claude verwendet wieder pip 😞
Session 3: "Ich hab's dir doch gesagt!" 😤
```

### Die Lösung

```
Session 1: "Verwende uv statt pip" → /reflect → Skill aktualisiert
Session 2: Claude verwendet uv ✅
Session 3: Claude verwendet uv ✅
Session N: Claude verwendet uv ✅
```

---

## 🎯 Features

### Drei Nutzungsmodi

1. **Manual** - `/reflect` nach Bedarf
2. **Automatic** - Läuft bei jedem Session-Ende (wenn aktiviert)
3. **Toggle** - Ein/Aus mit `/reflect-on` und `/reflect-off`

### Confidence Levels

- 🔴 **HIGH** - Explizite Korrekturen ("Verwende X statt Y")
- 🟡 **MEDIUM** - Approvals ("Ja, perfekt!")
- 🟢 **LOW** - Überlegungen ("Have you considered...")

### Sicherheit

- ✅ Timestamped Backups vor jedem Update
- ✅ YAML-Validation
- ✅ Automatischer Rollback bei Fehlern
- ✅ Git-Integration mit descriptiven Commit-Messages

---

## 📂 Struktur

```
reflect/
├── README.md                  # Diese Datei
├── USER_GUIDE.md             # Ausführlicher Guide (START HIER!)
├── SKILL.md                  # Skill-Definition
├── scripts/
│   ├── reflect.py            # Haupt-Engine
│   ├── extract_signals.py    # Pattern-Detection
│   ├── update_skill.py       # Safe Skill-Updates
│   ├── present_review.py     # Interactive Review
│   ├── hook-stop.sh          # Auto-Trigger Hook
│   ├── toggle-on.sh          # Aktivierung
│   ├── toggle-off.sh         # Deaktivierung
│   └── toggle-status.sh      # Status
├── .state/
│   ├── auto-reflection.json  # Toggle-Status
│   └── last-reflection.timestamp
└── references/
    └── signal-patterns.md    # Pattern-Library
```

---

## 📖 Dokumentation

### **➡️ [USER_GUIDE.md](USER_GUIDE.md) - LESEN SIE DIES ZUERST!**

Der vollständige Guide enthält:

- ✅ Detaillierte Erklärung aller Modi
- ✅ Praktische Beispiele
- ✅ Best Practices
- ✅ Troubleshooting
- ✅ FAQ
- ✅ Erweiterte Nutzung

### Quick Links

| Thema | Link |
|-------|------|
| **Quick Start** | [USER_GUIDE.md#quick-start](USER_GUIDE.md#quick-start) |
| **Drei Modi** | [USER_GUIDE.md#die-drei-nutzungsmodi](USER_GUIDE.md#die-drei-nutzungsmodi) |
| **Beispiele** | [USER_GUIDE.md#praktische-beispiele](USER_GUIDE.md#praktische-beispiele) |
| **Troubleshooting** | [USER_GUIDE.md#troubleshooting](USER_GUIDE.md#troubleshooting) |
| **FAQ** | [USER_GUIDE.md#faq](USER_GUIDE.md#faq) |

---

## 🎬 Beispiel-Workflow

### 1. Korrektur in Session

```
User: Erstelle ein Python-Projekt

Claude: Ich verwende pip install...

User: Nein, verwende uv statt pip. Uv ist schneller.

Claude: Ok, verwende jetzt uv install...
```

### 2. Reflection ausführen

```bash
/reflect
```

### 3. Review

```
═══════════════════════════════════════
REFLECTION REVIEW
═══════════════════════════════════════

## Signals Detected

**python-project-creator**:
  - HIGH: 1 corrections

## python-project-creator

```diff
+## Critical Corrections
+
+**Use 'uv' instead of 'pip'**
+
+- ✗ Don't: pip install
+- ✓ Do: uv install
```

[A]pprove / [M]odify / [S]kip / [Q]uit? A

✓ Approved changes to python-project-creator
✓ Updated python-project-creator
✓ Changes committed to git
```

### 4. Zukünftige Sessions

Claude verwendet automatisch `uv` statt `pip`! ✨

---

## 🛠️ Installation & Setup

Das System ist bereits installiert! Konfiguriert in:

- **Skills**: `~/.claude/skills/reflect/`
- **Hooks**: `~/.claude/settings.local.json`
- **Git**: `~/.claude/skills/.git/`

Prüfen Sie den Status:

```bash
/reflect-status
```

---

## ⚙️ Konfiguration

### Auto-Reflection aktivieren

```bash
/reflect-on
```

**Empfohlung**: Nutzen Sie zuerst den manuellen Modus (`/reflect`), um das System kennenzulernen.

### Hook-Konfiguration prüfen

```bash
cat ~/.claude/settings.local.json | grep -A 10 hooks
```

Sollte enthalten:

```json
"hooks": {
  "Stop": [{
    "hooks": [{
      "command": "/Users/.../.claude/skills/reflect/scripts/hook-stop.sh",
      "timeout": 5000
    }]
  }]
}
```

---

## 🔍 Monitoring & Debugging

### Git-History ansehen

```bash
cd ~/.claude/skills
git log --oneline --grep="reflection"
```

### Hook-Logs prüfen

```bash
tail -f ~/.claude/reflect-hook.log
```

### Backups finden

```bash
ls -lt ~/.claude/skills/{skill-name}/.backups/
```

### Status-Check

```bash
/reflect-status
```

---

## 🎓 Empfohlener Lernpfad

### Woche 1: Manual Mode

- Täglich `/reflect` nach Sessions mit Korrekturen
- Verstehen Sie die drei Confidence Levels
- Lesen Sie die Diffs sorgfältig
- Experimentieren Sie mit [A]pprove / [S]kip

**Ziel**: System verstehen und vertrauen aufbauen

### Woche 2: Semi-Automatic

- Weiter manuell, aber öfter
- Git-History regelmäßig prüfen
- Patterns erkennen

**Ziel**: Learnings akkumulieren

### Ab Woche 3: Automatic Mode

```bash
/reflect-on
```

- Läuft automatisch bei Session-Ende
- Prüfen Sie wöchentlich die Git-History
- Bei Bedarf: `/reflect-off` für kritische Sessions

**Ziel**: Kontinuierliches Lernen ohne manuelle Intervention

---

## 📊 Pattern-Erkennungs-Beispiele

### HIGH Confidence (Korrekturen)

```
✅ "Nein, verwende X statt Y"
✅ "Tatsächlich ist es X, nicht Y"
✅ "Niemals X tun"
✅ "Immer Y prüfen"
```

### MEDIUM Confidence (Approvals)

```
✅ "Ja, perfekt!"
✅ "Das funktioniert gut"
✅ "Genau so sollte es sein"
```

### LOW Confidence (Überlegungen)

```
✅ "Have you considered X?"
✅ "Was ist mit Y?"
✅ "Warum nicht Z verwenden?"
```

---

## 🚨 Troubleshooting Quick Ref

| Problem | Lösung |
|---------|--------|
| Keine Signale erkannt | Deutlichere Korrekturen, siehe [Patterns](#pattern-erkennungs-beispiele) |
| Skill nicht aktualisiert | Backup prüfen: `~/.claude/skills/{skill}/.backups/` |
| Git-Commit schlägt fehl | Manuell: `cd ~/.claude/skills && git commit -m "..."` |
| Auto-Reflection läuft nicht | Hook prüfen: `cat ~/.claude/reflect-hook.log` |
| Rollback nötig | `cd ~/.claude/skills && git revert HEAD` |

**Mehr Details**: [USER_GUIDE.md#troubleshooting](USER_GUIDE.md#troubleshooting)

---

## 🔗 Commands Cheat Sheet

| Command | Beschreibung |
|---------|--------------|
| `/reflect` | Manuelle Analyse der Session |
| `/reflect <skill>` | Analysiere nur einen Skill |
| `/reflect-on` | Auto-Reflection aktivieren |
| `/reflect-off` | Auto-Reflection deaktivieren |
| `/reflect-status` | Status anzeigen |

### Review-Optionen

| Taste | Aktion |
|-------|--------|
| `A` | Approve - Alle Änderungen übernehmen |
| `M` | Modify - Mit Natural Language modifizieren |
| `S` | Skip - Diesen Skill überspringen |
| `Q` | Quit - Review abbrechen |

---

## 🤝 Contributing

### Custom Patterns hinzufügen

Editieren Sie `scripts/extract_signals.py`:

```python
CORRECTION_PATTERNS = [
    r"(?i)no,?\s+don't\s+(?:do|use)\s+(.+?)[,.]?\s+(?:do|use)\s+(.+)",
    r"(?i)YOUR_PATTERN_HERE",  # ← Fügen Sie hier hinzu
]
```

### Pattern-Library erweitern

Dokumentieren Sie neue Patterns in:
```
references/signal-patterns.md
```

---

## 📜 Lizenz

Dieses Skill ist Teil von Claude Code.

---

## 🙏 Credits

Inspiriert von dem Konzept "Correct once, never again" aus der Developer Community.

Entwickelt für Claude Code mit ❤️

---

## 📞 Support

- **Ausführlicher Guide**: [USER_GUIDE.md](USER_GUIDE.md)
- **Pattern-Referenz**: [references/signal-patterns.md](references/signal-patterns.md)
- **Issue**: Bei Problemen Claude Code Issues melden

---

## 🎯 Nächste Schritte

1. **Lesen Sie**: [USER_GUIDE.md](USER_GUIDE.md)
2. **Status prüfen**: `/reflect-status`
3. **Erste Reflection**: Arbeiten Sie mit Claude → Korrigieren Sie etwas → `/reflect`
4. **Git-History ansehen**: `cd ~/.claude/skills && git log --oneline`
5. **Bei Gefallen**: `/reflect-on` für Auto-Modus

**Happy Learning!** 🚀

---

*Version: 1.0.0 | Erstellt: 2026-01-05*
