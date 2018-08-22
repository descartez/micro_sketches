from microbit import *

flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]
display.show(flash, delay=100)

while True:
    display.scroll("PickOdo.com")
    display.show(flash, delay=100)
    sleep(300)
    display.show(flash, delay=100)


