import pyautogui
import numpy as np
import cv2
import pygame
import time
import os

pygame.mixer.init()

def play_alert_minimap():
    filename = "minimap_warning.mp3"
    if not os.path.exists(filename):
        print("Missing minimap_warning.mp3 file.")
        return
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    time.sleep(2)

def run_minimap_alert(stop_event):
    region = (19, 1081, 356, 334)

    lower_red_1 = np.array([0, 150, 150])
    upper_red_1 = np.array([10, 255, 255])
    lower_red_2 = np.array([170, 150, 150])
    upper_red_2 = np.array([180, 255, 255])

    red_threshold = 5000
    check_interval = 0.1
    alert_cooldown = 4.5
    change_frozen = False
    last_red_mask = None
    last_alert_time = 0

    print("Minimap scanner running...")

    while not stop_event.is_set():
        screenshot = pyautogui.screenshot(region=region)
        frame = np.array(screenshot)

        hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
        mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
        red_mask = cv2.bitwise_or(mask1, mask2)

        if last_red_mask is not None:
            diff = cv2.absdiff(red_mask, last_red_mask)
            red_change = np.sum(diff)
            now = time.time()

            if red_change > red_threshold:
                if not change_frozen and now - last_alert_time >= alert_cooldown:
                    print("Enemy activity detected!")
                    play_alert_minimap()
                    last_alert_time = now
                    change_frozen = True
            elif red_change < 500:
                change_frozen = False

        last_red_mask = red_mask
        time.sleep(check_interval)
