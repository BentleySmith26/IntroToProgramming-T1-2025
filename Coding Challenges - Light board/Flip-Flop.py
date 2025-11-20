from adafruit_circuitplayground import cp

while True:
    if cp.switch == True:
        cp.pixels.brightness = 0.1
        for i in range(5):
            cp.pixels[i] = (0, 255, 0)
        for i in range(5, 10):
            cp.pixels[i] = (0, 0, 0)
    else:
        cp.pixels.brightness = 0.1
        for i in range(5, 10):
            cp.pixels[i] = (0, 255, 0)
        for i in range(5):
            cp.pixels[i] = (0, 0, 0)