import torch
import numpy as np
import cv2
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')


def generate_mask(img_path):
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
        # take first ear
        ear = ears[0]
        print(ear)

        # return mask
        mask = np.zeros(src.shape)
        mask[int(ear[1]):int(ear[3]), int(ear[0]):int(ear[2])] = 1
        return mask


# mask = generate_mask('0510.png')
# cv2.imwrite('mask0.png', mask*255)