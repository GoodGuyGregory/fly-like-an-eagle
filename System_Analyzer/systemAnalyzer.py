import pyautogui
import time
import random 
import sys

pyautogui.FAILSAFE = False

def switch_screens() -> None:
    max_switches = random.randint(1,5)
    pyautogui.keyDown('alt')
    
    for _ in range(1, max_switches):
        pyautogui.press('tab')
    
    pyautogui.keyUp('alt')
    
    
    
def move() -> None:
    
    max_moves = random.randint(4,9)
    
    for _ in range(1, max_moves):
        coords = get_random_coords()
        pyautogui.moveTo(
            x=coords[0],
            y=coords[1],
            duration=5
        )
        time.sleep(10)

def get_random_coords() -> []:
    screen = pyautogui.size()
    width = screen[0]
    height = screen[1]
    
    return [
        random.randint(100, width - 200),
        random.randint(100,height-200)
    ]

def main():
    print('Press Ctrl-C to quit.')
    
    try:
        while True:
            switch_screens()
            move()
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n")
        


main()
