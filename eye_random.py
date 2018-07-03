from microbit import *
import random

eyelid = Image("05550:"
                "50005:"
                "00000:"
                "50005:"
                "05550")
sensitivity = 500
wait_period = 1500

def draw_pupil(x,y):
    display.set_pixel(x,y,9)
    sleep(wait_period)

while True:
    x = random.randint(1,3)
    y = random.randint(1,3)

    display.show(eyelid)
    draw_pupil(x,y)