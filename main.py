
import time
import pyautogui
from PIL import ImageGrab
from threading import Thread


def main():
    thread = Thread(target=screenshotT1)
    thread.start()


def screenshotT1():
    # wait three seconds
    time.sleep(5)
    # take a screenshot    
    im1 = pyautogui.screenshot()
    # save it
    im1.save('my_screenshot.png')
    # send it to a server
    
    
    


def screenshotT2():
    myscreen = ImageGrab.grab()
    myscreen.save('myscreen_PIL.png')


main()
