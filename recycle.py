import os
import pyautogui

def recycle():
    try:
        os.chdir(r"C:\Users\Enter user here\Desktop") #enter your user 
        cwd = os.getcwd()
        result = cwd
        if result == 'C:\\Users\\Enter user here\\Desktop': #enter user here
            print("change was successfull!")
    except FileNotFoundError:
        print("Can't find directory\n check your directory input")
        
    recycle_bin = pyautogui.locateCenterOnScreen(r'C:\Users\Enter user here\Desktop\python\recycle.png', grayscale=False)
    pyautogui.rightClick(recycle_bin)
    empty_bin = pyautogui.locateCenterOnScreen(r'C:\Users\Enter user here\Desktop\python\empty.png')
    pyautogui.click(empty_bin)
    yes = pyautogui.locateCenterOnScreen(r'C:\Users\Enter user here\Desktop\python\yes.png', grayscale=False)
    pyautogui.press(['enter'])

recycle()
