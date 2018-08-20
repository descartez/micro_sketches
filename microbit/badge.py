from microbit import *

flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]
display.show(flash, delay=100)
accelerometerRunning= False

while True:
    if accelerometer.was_gesture("shake") and accelerometerRunning:
        display.show(flash, delay=100, wait=False)
    if button_b.is_pressed() and accelerometerRunning == False:
        accelerometerRunning = True
    elif button_b.is_pressed() and accelerometerRunning == True:
        accelerometerRunning = False

