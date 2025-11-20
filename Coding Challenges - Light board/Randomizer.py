from adafruit_circuitplayground import cp
import random


while True:
    cp.pixels.brightness = 0.01
    x, y, z = cp.acceleration
    shake_threshold = 15.0
    for i in range(0, 10):
        if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
            randx = random.randint(0, 255)
            randy = random.randint(0, 255)
            randz = random.randint(0, 255)
            cp.pixels[i] = (randx, randy, randz)