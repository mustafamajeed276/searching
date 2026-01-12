
import ctypes
import time
import threading

# Constants for mouse_event
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP   = 0x0004

user32 = ctypes.windll.user32

# Interval between clicks (seconds)
CLICK_INTERVAL = 0.625

# Flags and locks
running = False
running_lock = threading.Lock()
program_running = True

def clicker():
    """Thread that performs clicks when running is True."""
    global running, program_running
    while program_running:
        with running_lock:
            active = running
        if active:
            # Left button down
            user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            # small gap so OS registers down/up properly
            user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            # wait for next click
            # use sleep but be interruptible for quick toggles by checking running each 0.01s
            waited = 0.0
            while waited < CLICK_INTERVAL:
                time.sleep(0.01)
                waited += 0.01
                with running_lock:
                    if not running:
                        break
        else:
            # not active -> sleep a tiny bit to keep CPU low but responsive
            time.sleep(0.02)

def monitor_keys():
    """Monitor R key to toggle, and END to quit."""
    global running, program_running
    VK_R = 0x52      # virtual-key code for 'R'
    VK_END = 0x23    # virtual-key code for END key

    # We implement edge detection so one press toggles once.
    r_down_prev = False
    end_down_prev = False

    while program_running:
        # GetAsyncKeyState returns a short; high-order bit set when key currently down
        r_state = (user32.GetAsyncKeyState(VK_R) & 0x8000) != 0
        end_state = (user32.GetAsyncKeyState(VK_END) & 0x8000) != 0

        # Toggle on R press (edge: not down prev, now down)
        if r_state and not r_down_prev:
            with running_lock:
                running = not running
            print(f"Autoclicker {'ON' if running else 'OFF'}")
            # small debounce
            time.sleep(0.12)

        # Quit on END press
        if end_state and not end_down_prev:
            program_running = False
            print("Quitting autoclicker...")
            break

        r_down_prev = r_state
        end_down_prev = end_state
        time.sleep(0.01)


if __name__ == "__main__":
    print("Autoclicker starting.")
    print("Press 'R' to toggle ON/OFF. Press 'END' to quit.")
    click_thread = threading.Thread(target=clicker, daemon=True)
    click_thread.start()
    try:
        monitor_keys()
    except KeyboardInterrupt:
        program_running = False
    # wait briefly for thread to finish
    time.sleep(0.1)
    print("Stopped.")