from adafruit_circuitplayground import cp
import time

x = 0
while True:
    cp.pixels.brightness = 0.01
    if cp.button_a:
        cp.pixels.fill((0, 0, 0))
        x += 1
        if x > 10:
            x = 10
        for i in range(x):
            cp.pixels[i] = (255, 255, 255)
        time.sleep(0.2)
        while cp.button_a:
            pass
    if cp.button_b:
        cp.pixels.fill((0, 0, 0))
        x -= 1
        if x < 0:
            x = 0
        for i in range(x):
            cp.pixels[i] = (255, 255, 255)
        time.sleep(0.2)
        while cp.button_b:
            pass