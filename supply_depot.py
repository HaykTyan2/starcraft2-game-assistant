import pyautogui
import pytesseract
from PIL import Image
import time
import re
import pygame
import os

# Path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Region of screen where your supply appears (adjust for your resolution)
region = (2350, 25, 160, 50)

# Initialize pygame mixer for audio playback
pygame.mixer.init()

def play_alert():
    filename = "supply_warning.mp3"
    if not os.path.exists(filename):
        print("❌ Missing supply_warning.mp3 file. Run generate_voice.py first.")
        return

    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(0.2)  # 🔉 Set volume to 20%
    pygame.mixer.music.play()

    start = time.time()
    while pygame.mixer.music.get_busy() and time.time() - start < 2:
        time.sleep(0.01)  # ⚡ Quicker response loop

def get_supply():
    screenshot = pyautogui.screenshot(region=region)
    gray = screenshot.convert('L')
    text = pytesseract.image_to_string(gray)
    print("OCR Text:", text.strip())

    match = re.search(r'(\d+)\s*/\s*(\d+)', text)
    if match:
        current = int(match.group(1))
        maximum = int(match.group(2))
        return current, maximum
    return None, None

# 👁️ Start monitoring only after supply goes past 30/30
monitoring = False

while True:
    used, max_supply = get_supply()
    if used and max_supply:
        if not monitoring:
            # Activate monitoring after initial supply grows past 30/30
            if used > 30 and max_supply > 30:
                print(f"✅ Supply monitoring started: {used}/{max_supply}")
                monitoring = True
        elif monitoring:
            if max_supply - used <= 4 and max_supply < 200 and used < 194:
                print(f"⚠️ Supply warning: {used}/{max_supply}")
                play_alert()
                time.sleep(10)  # Cooldown to prevent spam
    time.sleep(1.5)
