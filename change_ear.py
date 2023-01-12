import tkinter as tk
import cv2
import numpy as np
import torch
import tkinter.filedialog
from PIL import Image, ImageTk
from tkinter import ttk, Frame


from inpainting import inpaint

def generate_mask(img_path):
    print("")
    print("Searching for ears in image: " + img_path)
    # Load Model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolo/yolo5s.pt')
    # Load image
    src = cv2.imread(img_path)
    # Inference
    results = model(img_path)

    ears = results.xyxy[0]

    # find matching ear
    if ears.shape[0] == 0:
        # if no ears detected -> return black mask
        return np.zeros(src.shape)
    else:
        print("Found " + str(len(ears)) + " ears")
        # take first ear
        ear = ears[0]

        # return mask
        mask = np.zeros(src.shape)
        mask[int(ear[1]):int(ear[3]), int(ear[0]):int(ear[2])] = 1

        print("")
        print("")
        return mask

# create main window
root = tk.Tk()
root.title("Change Ear")
root.config(bg="#212121")


top_frame = Frame(root, width=1200, height=200)
top_frame.grid(row=0, column=0, padx=5, pady=5)
top_frame.config(bg="#212121")

bottom_frame = Frame(root, width=1200, height=1200)
bottom_frame.grid(row=1, column=0, padx=5, pady=5)
bottom_frame.config(bg="#212121")

left_frame = Frame(bottom_frame, width=520, height=520)
left_frame.grid(row=0, column=0, padx=5, pady=5)
left_frame.config(bg="#191919")

right_frame = Frame(bottom_frame, width=520, height=520)
right_frame.grid(row=0, column=1, padx=5, pady=5)
right_frame.config(bg="#191919")


# create input field for image path
input_field = ttk.Entry(top_frame, justify=tk.LEFT)
input_field.config(width=80)
input_field.grid(row=0, column=1, padx=5, pady=5)

input_label = None
output_label = None

# create "browse" button
browse_button = ttk.Button(top_frame, text="Browse", command=lambda: choose_file())
browse_button.grid(row=0, column=0, padx=5, pady=5)

# create inpaint button
inpaint_button = ttk.Button(top_frame, text="Change Ear", command=lambda: inpaint_ear(input_field.get()))
inpaint_button.grid(row=1, column=0, padx=5, pady=5)



def choose_file():
    # open file dialog and set selected file as input
    filepath = tkinter.filedialog.askopenfilename()
    input_field.delete(0, tk.END)
    input_field.insert(0, filepath)

    # resize image to 512x512 and save resized image with PIL by first croping to square
    img = Image.open(input_field.get())
    img = img.crop((0, 0, min(img.size), min(img.size)))
    img = img.resize((512, 512))
    img.save("init0.png")

    # update input image label
    change_input_image()


def inpaint_ear(input_path):
    img = Image.open(input_path)
    img = img.crop((0, 0, min(img.size), min(img.size)))
    img = img.resize((512, 512))
    img.save("init0.png")

    # generate mask for ear
    mask = generate_mask("init0.png")
    cv2.imwrite('mask0.png', mask*255)

    # inpaint ear
    generated = inpaint("init0.png", "mask0.png").convert("RGB")
    generated.save("output0.png")

    # update input and output image labels
    change_input_image()
    change_output_image()

def change_input_image():
    # create label for input image
    global input_label
    input_label = tk.Label(left_frame)
    input_label.grid(row=0, column=0, padx=0, pady=0)
    input_label.config(width=512, height=512)

    input_image = Image.open("init0.png")
    input_image = ImageTk.PhotoImage(input_image)
    input_label.config(image=input_image)
    input_label.image = input_image

def change_output_image():
    # create label for output image
    global output_label
    output_label = tk.Label(right_frame)
    output_label.grid(row=0, column=0, padx=0, pady=0)
    output_label.config(width=512, height=512)

    output_image = Image.open("output0.png")
    output_image = ImageTk.PhotoImage(output_image)
    output_label.config(image=output_image)
    output_label.image = output_image

# start event loop
root.mainloop()
