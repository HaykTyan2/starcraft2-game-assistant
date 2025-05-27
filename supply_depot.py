import pyautogui
import pytesseract
from PIL import Image
import time
import re
import pygame
import os

pygame.mixer.init()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def play_alert_supply():
    filename = "supply_warning.mp3"
    if not os.path.exists(filename):
        print("Missing supply_warning.mp3 file.")
        return

    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

    start = time.time()
    while pygame.mixer.music.get_busy() and time.time() - start < 2:
        time.sleep(0.01)

def run_supply_monitor():
    region = (2350, 25, 160, 50)
    monitoring = False

    while True:
        screenshot = pyautogui.screenshot(region=region)
        gray = screenshot.convert('L')
        text = pytesseract.image_to_string(gray)
        print("OCR Text:", text.strip())

        match = re.search(r'(\d+)\s*/\s*(\d+)', text)
        if match:
            used = int(match.group(1))
            max_supply = int(match.group(2))

            if not monitoring:
                if used > 30 and max_supply > 30:
                    print(f"Supply monitoring started: {used}/{max_supply}")
                    monitoring = True
            elif max_supply - used <= 4 and max_supply < 200 and used < 194:
                print(f"Supply warning: {used}/{max_supply}")
                play_alert_supply()
                time.sleep(10)
        time.sleep(1.5)
