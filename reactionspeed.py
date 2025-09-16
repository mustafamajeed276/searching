import ctypes

# Windows API
hdc = ctypes.windll.user32.GetDC(0)
SendInput = ctypes.windll.user32.SendInput
GetCursorPos = ctypes.windll.user32.GetCursorPos

# Structures
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

PUL = ctypes.POINTER(ctypes.c_ulong)
class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL))
class INPUT(ctypes.Structure):
    _fields_ = (("type", ctypes.c_ulong),
                ("mi", MOUSEINPUT))

# Mouse flags
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP   = 0x0004

def click():
    inp = INPUT(type=0, mi=MOUSEINPUT(0,0,0,MOUSEEVENTF_LEFTDOWN,0,None))
    SendInput(1, ctypes.byref(inp), ctypes.sizeof(inp))
    inp = INPUT(type=0, mi=MOUSEINPUT(0,0,0,MOUSEEVENTF_LEFTUP,0,None))
    SendInput(1, ctypes.byref(inp), ctypes.sizeof(inp))

def get_pixel(x, y):
    color = ctypes.windll.gdi32.GetPixel(hdc, x, y)
    r = color & 0xff
    g = (color >> 8) & 0xff
    b = (color >> 16) & 0xff
    return (r,g,b)

# Loop
while True:
    pt = POINT()
    GetCursorPos(ctypes.byref(pt))  # get current mouse pos
    r,g,b = get_pixel(pt.x, pt.y)
    
    if g > 150 and r < 100 and b < 100:  # green detection
        click()