from tkinter import *

root = Tk()  # create root window
root.title("Frame Example")
root.config(bg="#212121")

# Create Frame widget
top_frame = Frame(root, width=1200, height=200)
top_frame.grid(row=0, column=0, padx=10, pady=5)
top_frame.config(bg="#212121")

bottom_frame = Frame(root, width=1200, height=1200)
bottom_frame.grid(row=1, column=0, padx=10, pady=5)
bottom_frame.config(bg="#212121")

left_frame = Frame(bottom_frame, width=520, height=520)
left_frame.grid(row=1, column=0, padx=10, pady=5)
left_frame.config(bg="#191919")

right_frame = Frame(bottom_frame, width=520, height=520)
right_frame.grid(row=1, column=1, padx=10, pady=5)
right_frame.config(bg="#191919")

root.mainloop()