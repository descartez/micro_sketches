from microbit import *
eyelid = Image("05550:"
                "50005:"
                "00000:"
                "50005:"
                "05550")


while True:
    acc_x = accelerometer.get_x() // 20
    if acc_x > 0:
        x = 3
    elif acc_x < 0:
        x = 1
    else:
        x = 2

    acc_y = accelerometer.get_y() // 500
    if acc_y > 0:
        y = 3
    elif acc_y < 0:
        y = 1
    else:
        y = 2

    display.show(eyelid)
    display.set_pixel(x,y,9)
    sleep(500)
    display.set_pixel(x,y,0)
    display.set_pixel(x,y,9)
    sleep(500)