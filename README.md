# StarCraft II Game Assistant

A real-time assistant for StarCraft II using Python and OpenCV. It notices enemy units on the minimap and monitors your supply count in case the player did not see it or is distracted, giving timely audio alerts during gameplay.

I made this project to help my dad improve at StarCraft II — specifically to give him an edge in noticing enemy movements and managing his supply more efficiently.
He’s a solid player, but tends to get caught off guard or supply blocked at key moments. My goal was to give him a tool that boosts his awareness, so maybe (just maybe) he can finally break into Gold rank.

It also gave me a great excuse to explore computer vision, and Python automation in a fun and meaningful way.

Disclaimer:
This tool is not a cheat and does not modify or interfere with StarCraft II’s game code in any way. It functions purely as an external assistant that analyzes on-screen visual information to provide helpful reminders.
Its purpose is to alert players about their supply count or notify them of visible enemy units on the minimap—things they might have overlooked during gameplay.
It does not provide unfair advantages, automate gameplay, or access any game internals.



---------------------------------------------------------------------------------------------------------------------------------------------------

## Features

- 📍 Detects new red dots (enemy units) on the minimap
- 🔊 Plays warning audio when enemy activity is detected
- 📦 Monitors supply count and alerts when you’re near supply block

---------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠 Tech Stack

- Python
- OpenCV
- PyAutoGUI
- Pytesseract
- Pygame

------------------------------------------------------------------------------------------------------------------------------------------------
## How to Run / Prerequisites

- Python 3.7+
- Tesseract OCR must be installed on your system  
  [Download it here](https://github.com/tesseract-ocr/tesseract)

Update the path in `supply_depot.py` LIKE THIS:
```python
# Inside supply_depot.py
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
------------------------------------------------------------------------------------------------------------------------------------------------
(MAKE SURE YOU'RE IN THE CORRECT FOLDER BEFORE RUNNING IT)
Install dependencies with:


```bash
pip install -r requirements.txt
```
------------------------------------------------------------------------------------------------------------------------------------------------
(MAKE SURE YOU'RE IN THE CORRECT FOLDER BEFORE RUNNING IT)
Starting the Assistant:
Run this command in your terminal:

```
python main.py
```
------------------------------------------------------------------------------------------------------------------------------------------------
Audio Alerts
Two .mp3 files are used to provide audio warnings:

minimap_warning.mp3 – Played when new enemy units appear on the minimap

supply_warning.mp3 – Played when you're close to being supply blocked

These are already included. You can replace them or generate your own using the scripts in the /tools folder
------------------------------------------------------------------------------------------------------------------------------------------------
Optional: Customize Voice Alerts
Want your own voice lines? Use the Python scripts in the /tools folder:

/tools/generate_supply_voice.py
/tools/generate_minimap_voice.py
