import board
import digitalio

import time
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05)
pixels.fill((0, 0, 0))
pixels.show()


# make the 2 input buttons
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

flashlightSwitch = False

def flashlight():
    pixels.brightness = 1
    pixels.fill((255, 50, 0))

def pixelReset():
    pixels.brightness = 0.05
    pixels.fill((0, 0, 0))

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - (pos * 3)), 0, int(pos * 3))
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3))

def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int(i + j)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        if buttonA.value:
            break
        time.sleep(wait)

while True:
    if buttonA.value:
        pixelReset()
        flashlight()
    elif buttonB.value:
        pixelReset()
        rainbow(0.0001)

