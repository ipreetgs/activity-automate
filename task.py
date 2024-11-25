import pyautogui
import random
import time

# Safety feature adjustments
pyautogui.PAUSE = 0.1

# Initial variables
pattern_size = 5
distance_threshold = 200
directions = ["right", "down", "left", "up"]

def move_mouse(direction, distance):
    if direction == "right":
        pyautogui.moveRel(distance, 0, duration=distance / 1000)
    elif direction == "down":
        pyautogui.moveRel(0, distance, duration=distance / 1000)
    elif direction == "left":
        pyautogui.moveRel(-distance, 0, duration=distance / 1000)
    elif direction == "up":
        pyautogui.moveRel(0, -distance, duration=distance / 1000)

try:
    while True:
        direction = random.choice(directions)
        distance = random.randint(pattern_size // 2, pattern_size)

        try:
            move_mouse(direction, distance)
        except pyautogui.FailSafeException:
            print("Temporarily disabling fail-safe to move cursor to center.")
            pyautogui.FAILSAFE = False  # Temporarily disable fail-safe
            screenWidth, screenHeight = pyautogui.size()
            pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
            pyautogui.FAILSAFE = True  # Re-enable fail-safe
            continue

        pattern_size += 1
        if distance > distance_threshold:
            pattern_size = 5

        time.sleep(random.uniform(0.4, 0.8))

except KeyboardInterrupt:
    print("Program exited!")
