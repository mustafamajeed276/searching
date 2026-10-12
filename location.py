import ctypes
import colorsys
import time
from ctypes import wintypes

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

user32.SetProcessDPIAware()  # makes coordinates match real screen pixels

user32.GetDC.restype = wintypes.HDC
user32.GetDC.argtypes = [wintypes.HWND]
user32.ReleaseDC.argtypes = [wintypes.HWND, wintypes.HDC]
gdi32.GetPixel.restype = wintypes.COLORREF
gdi32.GetPixel.argtypes = [wintypes.HDC, ctypes.c_int, ctypes.c_int]

def is_green(r, g, b):
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    hue = h * 360
    return 75 <= hue <= 165 and s >= 0.25 and v >= 0.20

def get_pixel_under_mouse():
    pt = wintypes.POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    hdc = user32.GetDC(None)
    color = gdi32.GetPixel(hdc, pt.x, pt.y)
    user32.ReleaseDC(None, hdc)
    if color == 0xFFFFFFFF:  # failed to read
        return pt.x, pt.y, None
    r = color & 0xFF
    g = (color >> 8) & 0xFF
    b = (color >> 16) & 0xFF
    return pt.x, pt.y, (r, g, b)

def left_click():
    user32.mouse_event(0x0002, 0, 0, 0, 0)  # left button down
    user32.mouse_event(0x0004, 0, 0, 0, 0)  # left button up

print("Running. Move the mouse onto something green.")
print("Press ESC or Ctrl+C to stop.")

was_on_green = False

try:
    while not (user32.GetAsyncKeyState(0x1B) & 0x8000):  # 0x1B = ESC key
        x, y, rgb = get_pixel_under_mouse()
        on_green = rgb is not None and is_green(*rgb)

        if on_green and not was_on_green:
            left_click()
            print(f"Clicked at ({x}, {y}) on color RGB{rgb}")

        was_on_green = on_green
        time.sleep(0.01)
except KeyboardInterrupt:
    pass

print("Stopped.")