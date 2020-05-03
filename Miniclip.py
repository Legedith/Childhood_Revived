import usb_hid
import time
from adafruit_circuitplayground.express import cpx
from adafruit_hid.mouse import Mouse
from adafruit_circuitplayground import cp

m = Mouse(usb_hid.devices)
cpx.adjust_touch_threshold(200)
pix = cpx.pixels
pix.brightness = 0.4
while True:
    x, y, z = cpx.acceleration
    for i in range(10):
        print((abs(int(x))*10,abs(int(y))*10 ,abs(int(z))*10 ))
        pix[i] = (abs(int(x))*10 %255,abs(int(y))*10 %255,abs(int(z))*10 %255)
    if cpx.switch:
        continue

    cpx.red_led = True
    m.move(5*int(-x), 5*int(y), 0)
    if cp.button_a:
        m.click(Mouse.LEFT_BUTTON)

    if cp.button_b:
        m.click(Mouse.RIGHT_BUTTON)
    print(y)