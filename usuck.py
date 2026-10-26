"""
U SUCK message window.
Shows "U SUCK" in the middle of the screen until you press F.

Requires Python 3 with tkinter (included with most Python installs).

Run:
    python u_suck.py
"""

import tkinter as tk


def close_window(event=None):
    """Close the message when F is pressed."""
    root.destroy()


root = tk.Tk()
root.title("Message")
root.attributes("-fullscreen", True)
root.configure(bg="black")

label = tk.Label(
    root,
    text="U SUCK",
    font=("Arial", 96, "bold"),
    fg="red",
    bg="black",
)
label.place(relx=0.5, rely=0.5, anchor="center")

hint = tk.Label(
    root,
    text="Press F to close",
    font=("Arial", 18),
    fg="gray",
    bg="black",
)
hint.place(relx=0.5, rely=0.9, anchor="center")

root.bind("<f>", close_window)
root.bind("<F>", close_window)
root.focus_force()

root.mainloop()