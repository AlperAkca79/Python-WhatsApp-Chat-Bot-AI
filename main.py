import time
import pyautogui as gui

file = open("messages.txt", "r")

messages = file.readlines()
time.sleep(5)

gui.moveTo(700, 982)
gui.click()

for word in messages:
    gui.write(f"Your word {word}", interval=0.01)

    gui.press("enter")