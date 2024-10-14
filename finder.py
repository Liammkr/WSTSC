import pyautogui
from PIL import Image
def get_color_at_position(x, y):
    screenshot = pyautogui.screenshot(region=(x, y, 1, 1))
    color = screenshot.getpixel((0, 0))
    return color
import time
print("Move the mouse to the desired position within the next 5 seconds...")
time.sleep(5) 
x, y = pyautogui.position() 
color = get_color_at_position(x, y)
print(f"Color at position ({x}, {y}): {color}")
