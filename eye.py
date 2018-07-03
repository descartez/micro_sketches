from microbit import *
eyelid = Image("05550:"
                "50005:"
                "00000:"
                "50005:"
                "05550")
sensitivity = 500
wait_period = 200

def draw_pupil(prev_x, prev_y, x,y):
    display.set_pixel(x,y,9)
    sleep(wait_period)

while True:
    acc_x = accelerometer.get_x() // sensitivity
    if acc_x > 0:
        x = 3
    elif acc_x < 0:
        x = 1
    else:
        x = 2

    acc_y = accelerometer.get_y() // sensitivity
    if acc_y > 0:
        y = 3
    elif acc_y < 0:
        y = 1
    else:
        y = 2

    display.show(eyelid)
    draw_pupil(0,0,x,y)
    prev_x = x
    prev_y = y
    draw_pupil(prev_x,prev_y,x,y)