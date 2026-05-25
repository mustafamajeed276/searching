# Windows only — no external libraries needed
# Hold F to move the mouse in a perfect circle

import ctypes
import math
import time

# Windows API
user32 = ctypes.windll.user32

# Mouse position structure
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

def get_mouse_pos():
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

def set_mouse_pos(x, y):
    user32.SetCursorPos(int(x), int(y))

def key_pressed(vk_code):
    return user32.GetAsyncKeyState(vk_code) & 0x8000

# Settings
RADIUS = 150
SPEED = 0.002
SMOOTHNESS = 360

VK_F = 0x46  # Virtual key code for F

print("Hold F to move mouse in a perfect circle.")
print("Press CTRL+C to exit.")

while True:
    if key_pressed(VK_F):
        center_x, center_y = get_mouse_pos()

        while key_pressed(VK_F):
            for angle in range(SMOOTHNESS):
                if not key_pressed(VK_F):
                    break

                theta = math.radians(angle)

                x = center_x + RADIUS * math.cos(theta)
                y = center_y + RADIUS * math.sin(theta)

                set_mouse_pos(x, y)
                time.sleep(SPEED)

    time.sleep(0.01)