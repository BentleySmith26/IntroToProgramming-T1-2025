from adafruit_circuitplayground import cp

while True:
    cp.pixels.brightness = 0.1
    cp.pixels[0] = (0, 0, 255)
    temp_c = cp.temperature
    temp_f = ((temp_c * 9 / 5) + 32)
    for i,v in enumerate(cp.pixels):
        if temp_f >= 77 + i:
            cp.pixels[i] = (255 if i > 2 else 0, 255 if i > 2 and i < 7 else 0, 255 if i < 3 else 0)
        else:
            cp.pixels[i] = (0, 0, 0)