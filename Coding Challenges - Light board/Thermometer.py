from adafruit_circuitplayground import cp

while True:
    cp.pixels.brightness = 0.01
    cp.pixels[0] = (0, 0, 255)
    temp_c = cp.temperature
    temp_f = ((temp_c * 9 / 5) + 32) - 77
    if temp_f >= 1:
        cp.pixels[1] = (0, 0 ,255)
    if temp_f > 2:
        cp.pixels[2] = (0, 0, 255)
    if temp_f > 3:
        cp.pixels[3] = (255, 255, 0)
    if temp_f > 4:
        cp.pixels[4] = (255, 255, 0)
    if temp_f > 5:
        cp.pixels[5] = (255, 255, 0)
    if temp_f > 6:
        cp.pixels[6] = (255, 255, 0)
    if temp_f > 7:
        cp.pixels[7] = (255, 0, 0)
    if temp_f > 8:
        cp.pixels[8] = (255, 0, 0)
    if temp_f > 9:
        cp.pixels[9] = (255, 0, 0)
    for i in range(9, temp_f, -1):
        cp.pixels[i] = (0, 0, 0)