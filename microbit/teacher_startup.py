from microbit import *
import music

flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

music.play(music.POWER_UP)
display.show(Image.HAPPY)
sleep(350)

while True:
    if accelerometer.was_gesture("3g"):
        display.show(flash, delay=100, wait=False)
        music.play(music.BA_DING)
    if button_a.is_pressed():
        display.show(Image.ARROW_W)
        sleep(250)
        display.clear()
    if button_b.is_pressed():
        display.show(Image.ARROW_E)
        sleep(250)
        display.clear()
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(flash, delay=100, wait=False)