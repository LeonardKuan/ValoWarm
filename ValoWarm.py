import pyautogui
import time

import pyautogui
import time

# Function to perform a series of clicks and typing operations
def perform_operations():
    
    # Click into Deceive
    pyautogui.moveTo(495, 370, duration=1)
    pyautogui.click(clicks=2)
    time.sleep(2)
    
    # Click into Valorant # 121, 195
    pyautogui.moveTo(121, 195, duration=1)
    pyautogui.click(clicks=1)
    time.sleep(12)

    # Login
    pyautogui.typewrite("", interval=0.1)
    pyautogui.press('tab')
    pyautogui.typewrite("", interval=0.1)
    pyautogui.press('enter')
    
    # Click into Client's Play
    time.sleep(6)
    pyautogui.moveTo(374, 398, duration=1)
    pyautogui.click(clicks=1)
    
    # Click into Play 
    time.sleep(285)
    pyautogui.moveTo(175, 311, duration=1)
    pyautogui.click(clicks=1)
    
    # Click into Deathmatch
    time.sleep(3)
    pyautogui.moveTo(913, 74, duration=1)
    pyautogui.click(clicks=1)
    
    # Click into Queue
    time.sleep(3)
    pyautogui.moveTo(935, 976, duration=1)
    pyautogui.click(clicks=1)
    
    # Click into Play
    time.sleep(870)
    pyautogui.moveTo(175, 311, duration=1)
    pyautogui.click(clicks=1)
    
    # Click into Queue
    time.sleep(3)
    pyautogui.moveTo(935, 976, duration=1)
    pyautogui.click(clicks=1)

# Execute the function
perform_operations()