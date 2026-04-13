# Pokemon Battle CLI

A terminal-based Pokemon battle game written in Python, enhanced with AutoHotkey v2 scripts for automated input assistance.

---

## What It Does

Pokemon Battle CLI simulates a turn-based Pokemon battle in the Windows Command Prompt. Two Pokemon are randomly assigned, each with a type, moves, and HP. The player chooses actions each turn — attacking, using items, throwing Pokeballs, or running.

Two AutoHotkey scripts run alongside the game to assist with input:

- **`sendone.ahk`** — Automatically types `1` whenever the game is waiting for input, so the default option is always pre-filled.
- **`scroll.ahk`** — Allows the player to cycle through available options using `Alt+A`, incrementing the current selection and looping back around.

---

## Requirements

- Python 3.x
- [AutoHotkey v2](https://www.autohotkey.com/)
- Windows (Command Prompt)

---

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/kn5225/pokemon-battle-cli.git
   cd pokemon-battle-cli
   ```

2. Ensure AutoHotkey v2 is installed. Note the path to its executable (e.g. `C:\Program Files\AutoHotkey\v2\AutoHotkey64.exe`).

3. Update the AHK executable path in `poke.py` to match your system:
   ```python
   AHK = r"C:\Program Files\AutoHotkey\v2\AutoHotkey64.exe"
   ```

---

## Usage

Run the game with:

```
python poke.py
```

Python will automatically launch both AHK scripts and terminate them when the game ends or is interrupted.

**Controls:**
- Type a number and press `Enter` to confirm a choice
- Press `Alt+A` to cycle through the available options before confirming
- Press `Ctrl+C` to exit at any time

---

## File Structure

```
pokemon-battle-cli/
│
├── poke.py          # Main game logic
├── sendone.ahk      # Auto-fills default input when the game is waiting
├── scroll.ahk       # Alt+A hotkey to cycle through input options
└── .gitignore       # Excludes runtime files from version control
```

> **Note:** `input.txt`, `movnumwrite.txt`, and `tracker.txt` are generated automatically at runtime in the same directory. They are excluded from the repo via `.gitignore`.

---

## Notes

- The AHK scripts are launched and terminated by `poke.py` automatically — there is no need to run them separately.
- All file paths are relative, so the project works from any directory without modification beyond the AHK executable path.
- The game supports 18 Pokemon types with type-effectiveness logic built in.
- Move PP is tracked per move and depletes with use.
