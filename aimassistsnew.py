"""
Blue Snap Clicker (no installs needed - Windows only, standard library only)

When enabled, if your cursor gets within SEARCH_RADIUS pixels of any shade of
blue, the cursor snaps onto it and left-clicks once every 0.625 seconds for as
long as it stays on blue.

Hotkeys:
    N  - toggle on/off (starts OFF)
    F9 - quit
"""

import ctypes
import time
from ctypes import wintypes

# ---------------- Settings ----------------
SEARCH_RADIUS = 50       # px around the cursor to look for blue
STEP = 2                 # check every Nth pixel (higher = faster, less precise)
CLICK_INTERVAL = 0.625   # seconds between clicks
LOOP_DELAY = 0.01
CENTER_REFINE = 6        # px; centers the cursor inside the blue patch
MIN_BLUE_LEAD_R = 40     # blue must beat red by at least this much
MIN_BLUE_LEAD_G = 15     # ...and green by at least this much
MIN_SATURATION = 0.35    # (max-min)/max, filters out greys
MIN_BRIGHTNESS = 50      # blue channel must be at least this (ignores near-black)
# ------------------------------------------

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

try:
    user32.SetProcessDPIAware()  # make coordinates match real pixels
except Exception:
    pass

VK_N, VK_F9 = 0x4E, 0x78   # N = toggle, F9 = quit
SRCCOPY = 0x00CC0020


class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ("biSize", wintypes.DWORD), ("biWidth", wintypes.LONG),
        ("biHeight", wintypes.LONG), ("biPlanes", wintypes.WORD),
        ("biBitCount", wintypes.WORD), ("biCompression", wintypes.DWORD),
        ("biSizeImage", wintypes.DWORD), ("biXPelsPerMeter", wintypes.LONG),
        ("biYPelsPerMeter", wintypes.LONG), ("biClrUsed", wintypes.DWORD),
        ("biClrImportant", wintypes.DWORD),
    ]


def get_cursor():
    pt = wintypes.POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y


def key_down(vk):
    return bool(user32.GetAsyncKeyState(vk) & 0x8000)


def click():
    user32.mouse_event(0x0002, 0, 0, 0, 0)  # left down
    user32.mouse_event(0x0004, 0, 0, 0, 0)  # left up


def grab(left, top, w, h):
    """Capture a screen region; returns raw BGRA bytes."""
    screen_dc = user32.GetDC(0)
    mem_dc = gdi32.CreateCompatibleDC(screen_dc)
    bmp = gdi32.CreateCompatibleBitmap(screen_dc, w, h)
    old = gdi32.SelectObject(mem_dc, bmp)
    gdi32.BitBlt(mem_dc, 0, 0, w, h, screen_dc, left, top, SRCCOPY)

    bi = BITMAPINFOHEADER()
    bi.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bi.biWidth = w
    bi.biHeight = -h          # negative = top-down rows
    bi.biPlanes = 1
    bi.biBitCount = 32
    bi.biCompression = 0
    buf = ctypes.create_string_buffer(w * h * 4)
    gdi32.GetDIBits(mem_dc, bmp, 0, h, buf, ctypes.byref(bi), 0)

    gdi32.SelectObject(mem_dc, old)
    gdi32.DeleteObject(bmp)
    gdi32.DeleteDC(mem_dc)
    user32.ReleaseDC(0, screen_dc)
    return buf.raw


def is_blue(data, i):
    b, g, r = data[i], data[i + 1], data[i + 2]
    return (
        b >= MIN_BRIGHTNESS
        and b - r >= MIN_BLUE_LEAD_R
        and b - g >= MIN_BLUE_LEAD_G
        and b >= g and b >= r
        and (b - min(r, g)) / b >= MIN_SATURATION
    )


def find_nearest_blue(cx, cy):
    sw, sh = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    left = max(0, cx - SEARCH_RADIUS)
    top = max(0, cy - SEARCH_RADIUS)
    right = min(sw, cx + SEARCH_RADIUS + 1)
    bottom = min(sh, cy + SEARCH_RADIUS + 1)
    w, h = right - left, bottom - top
    if w <= 0 or h <= 0:
        return None

    data = grab(left, top, w, h)
    ox, oy = cx - left, cy - top
    r2 = SEARCH_RADIUS * SEARCH_RADIUS

    best, best_d = None, r2 + 1
    for y in range(0, h, STEP):
        dy = y - oy
        row = y * w
        for x in range(0, w, STEP):
            dx = x - ox
            d = dx * dx + dy * dy
            if d < best_d and is_blue(data, (row + x) * 4):
                best, best_d = (x, y), d
    if best is None:
        return None

    # Refine toward the middle of the local blue patch
    bx, by = best
    sx = sy = n = 0
    for y in range(max(0, by - CENTER_REFINE), min(h, by + CENTER_REFINE + 1)):
        for x in range(max(0, bx - CENTER_REFINE), min(w, bx + CENTER_REFINE + 1)):
            if is_blue(data, (y * w + x) * 4):
                sx += x
                sy += y
                n += 1
    if n:
        bx, by = round(sx / n), round(sy / n)
    return left + bx, top + by


def main():
    print("Blue Snap Clicker ready.  N = toggle, F9 = quit.")
    enabled = False
    n_prev = False
    last_click = 0.0

    while not key_down(VK_F9):
        n = key_down(VK_N)
        if n and not n_prev:
            enabled = not enabled
            print("ENABLED" if enabled else "DISABLED")
        n_prev = n

        if enabled:
            cx, cy = get_cursor()
            target = find_nearest_blue(cx, cy)
            if target:
                if target != (cx, cy):
                    user32.SetCursorPos(*target)
                now = time.perf_counter()
                if now - last_click >= CLICK_INTERVAL:
                    click()
                    last_click = now
        time.sleep(LOOP_DELAY)

    print("Bye.")


if __name__ == "__main__":
    main()