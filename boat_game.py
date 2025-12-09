import Tiny2 as tn
import random
import time
import keyboard 

width = 120
height = 35

Screen = tn.Screen(width,height)

Screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

x = 0
y = 0

while True:
    Screen.line((10,10),(10,20))

    Screen.render()
    time.sleep(0.1)