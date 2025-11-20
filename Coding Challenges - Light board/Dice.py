from adafruit_circuitplayground import cp
import time
import random


while True:
    cp.pixels.brightness = 0.01
    if cp.button_a:
        cp.pixels.fill((0, 0, 0))
        x = random.randint(1, 10)
        for i in range(x):
            cp.pixels[i] = (255, 0, 0)
        time.sleep(.2)
    if cp.button_b:
        cp.pixels.fill((0, 0, 0))