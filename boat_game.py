import Tiny2 as tn
import random
import time

Screen = tn.Screen(120,35)

Screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

x = 0
y = 0

while True:
    Screen.define(x,y,"☺",(255,0,0))
    x = x + 1
    y = y + 1
    if y >= 35:
        y = 0
    if x >= 120:
        x = 0
    
    Screen.render()
    time.sleep(1)