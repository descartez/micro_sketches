import digitalio
import board
import time
import array
import math
import audioio
import neopixel

FREQUENCY = 440  # 440 Hz middle 'A'
SAMPLERATE = 8000  # 8000 samples/second, recommended!

# Generate one period of sine wav.
length = SAMPLERATE // FREQUENCY
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15)

# enable the speaker
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True

audio = audioio.AudioOut(board.A0)
sine_wave_sample = audioio.RawSample(sine_wave)

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.DOWN

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

morphed = False
RED = 0x100000
YELLOW = (0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)
lights = [RED, YELLOW, GREEN, AQUA, BLUE, PURPLE]

def morph(wait):
    for i in range(len(pixels)):
        pixels[i] = YELLOW
        time.sleep(wait)
    time.sleep(0.1)

    pixels.fill(AQUA)
    time.sleep(0.01)
    pixels.fill(AQUA)
    time.sleep(0.01)
    pixels.fill(GREEN)

def clearLeds():
    pixels.fill(BLACK))
    pixels.show()

while True:
    if button_a.value:
        morph(0.01)
        audio.play(sine_wave_sample, loop=True)
        time.sleep(0.5)
        audio.stop()
        morphed = True
    while morphed:
        print("MORPHED")
        for i in range(len(pixels)):
            pixels.fill(GREEN)
            pixels[i] = BLUE
            if button_b.value:
                morphed = False
    clearLeds()
