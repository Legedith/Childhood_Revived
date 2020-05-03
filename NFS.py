from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from time import sleep
from adafruit_circuitplayground import cp
import usb_hid

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
pix = cpx.pixels
pix.brightness = 0.4
while True:
    x, y, z = cpx.acceleration
    for i in range(10):
        #print(int(x),int(y),int(z))
        pix[i] = (abs(int(x))*10 %255,abs(int(y))*10 %255,abs(int(z))*10 %255)
    if cpx.switch:
        continue

    if x>3:
        kbd.press(Keycode.LEFT_ARROW)
        sleep(0.2)
        kbd.release(Keycode.LEFT_ARROW)

    if x<-3:
        kbd.press(Keycode.RIGHT_ARROW)
        sleep(0.2)
        kbd.release(Keycode.RIGHT_ARROW)
    if y>3:
        kbd.press(Keycode.UP_ARROW)
        print("up")
        #sleep(0.2)
        #kbd.release(Keycode.UP_ARROW)
    if y<-4:
        kbd.release(Keycode.UP_ARROW)
        kbd.press(Keycode.DOWN_ARROW)
        sleep(1.2)
        kbd.release(Keycode.DOWN_ARROW)
    if y<2 and y>-4:
        print("released")
        kbd.release(Keycode.UP_ARROW)
    if cp.button_a:
        kbd.press(Keycode.X)
        sleep(0.2)
        kbd.release(Keycode.X)

    if cp.button_b:
        kbd.press(Keycode.Z)
        sleep(0.2)
        kbd.release(Keycode.Z)