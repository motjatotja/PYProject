import pyautogui as gui
import random
import time as t

print("Bot Running in background. Press ctrl + C to exit")

while True:
    x = random.randint(50,1200)
    y = random.randint(50,600)
    gui.moveTo(x,y,0.5)
    print("Ok")
    t.sleep(10)
