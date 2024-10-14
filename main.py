import pyautogui
import time
import subprocess
from datetime import datetime, timedelta
def press_number(number):
    pyautogui.write(f"{number:04d}") 
    pyautogui.press('enter') 
def click_positions(x1, y1, x2, y2):
    pyautogui.moveTo(x1, y1) 
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(x2, y2)
    time.sleep(1) 
    pyautogui.click() 
def advance_by_days(days):
    current_date_time = datetime.now()
    new_date_time = current_date_time + timedelta(days=days)
    formatted_date_time = new_date_time.strftime("%m%d%H%M%y")
    subprocess.run(["sudo", "date", formatted_date_time], check=True)
    print(f"Date advanced")
def is_color_in_centered_area(center_x, center_y, width, height, target_color):
    x = center_x - width // 2
    y = center_y - height // 2
    region = (x, y, width, height)
    screenshot = pyautogui.screenshot(region=region)
    for i in range(width):
        for j in range(height):
            current_color = screenshot.getpixel((i, j))
            if current_color[:3] == target_color:  
                return True 
    return False 
def check_if_correct():
    center_x, center_y = 869, 523 
    width, height = 200, 100 
    target_color = (192, 72, 60) 
    if not is_color_in_centered_area(center_x, center_y, width, height, target_color):
        return True 
    return False
def main():
    days_to_advance = 1  
    for i in range(10000):  
        press_number(i)
        print(f"Tried: {i:04d}")    
        time.sleep(1)
        if check_if_correct():  
            print(f"Correct code found: {i:04d}")
            break
        advance_by_days(days_to_advance)
        time.sleep(1)
        click_positions(975, 599, 1128, 704) 
        time.sleep(0.5)

if __name__ == "__main__":
    time.sleep(5)  
    main()
