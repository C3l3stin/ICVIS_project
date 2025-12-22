import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import cv2
import yaml
import shutil
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset
from PIL import Image
import torch

# print(torch.cuda.is_available())







def pair_split(image_split_dir, label_split_dir):
    pairs = []
    for img in os.listdir(image_split_dir):
        if img.lower().endswith(('.jpg', '.png', '.jpeg')):
            label = os.path.splitext(img)[0] + ".txt"
            label_path = os.path.join(label_split_dir, label)
            if os.path.exists(label_path):
                pairs.append((os.path.join(image_split_dir, img), label_path))
    return pairs


def display_image_with_bboxes(img, targets):
    print(f"Number of objects in this image: {len(targets)}")
    # COCO stores bbox as [x, y, width, height]
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.imshow(img)  # CHW -> HWC

    for t in targets:
        x, y, w, h = t.numpy()
        rect = patches.Rectangle(
            (x, y),
            w,
            h,
            linewidth=2,
            edgecolor="red",
            facecolor="none",
        )
        ax.add_patch(rect)

    plt.axis("off")
    plt.show()