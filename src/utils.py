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
    ax.imshow(img.permute(1, 2, 0))  # CHW -> HWC

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

    import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_yolo_sample(img_tensor, label_matrix, S=7):
    # 1. Préparer l'image : [C, H, W] -> [H, W, C]
    img = img_tensor.permute(1, 2, 0).cpu().numpy()
    
    fig, ax = plt.subplots(1, figsize=(8, 8))
    ax.imshow(img)
    
    H, W, _ = img.shape

    # 2. Dessiner la grille (optionnel, pour debug)
    for l in range(S + 1):
        ax.axhline(l * (H/S), color='white', lw=0.5, alpha=0.3)
        ax.axvline(l * (W/S), color='white', lw=0.5, alpha=0.3)

    # 3. Parcourir la grille
    for i in range(S):     # Lignes (y)
        for j in range(S): # Colonnes (x)
            # On vérifie si un objet est présent (confiance == 1)
            if label_matrix[i, j, 4] == 1:
                # Récupérer les coordonnées relatives à la cellule
                x_cell, y_cell, w, h = label_matrix[i, j, 0:4]
                
                # Reconvertir en coordonnées normalisées globales (0 à 1)
                xc = (x_cell + j) / S
                yc = (y_cell + i) / S
                
                # Convertir en pixels pour Matplotlib
                # (YOLO utilise le centre, Matplotlib utilise le coin haut-gauche)
                width_pix = w * W
                height_pix = h * H
                x_min = (xc * W) - (width_pix / 2)
                y_min = (yc * H) - (height_pix / 2)
                
                # Créer le rectangle
                rect = patches.Rectangle(
                    (x_min, y_min), width_pix, height_pix, 
                    linewidth=2, edgecolor='red', facecolor='none'
                )
                ax.add_patch(rect)
                
                # Ajouter un petit point au centre pour vérifier la cellule
                ax.plot(xc * W, yc * H, 'ro', markersize=3)

    plt.title(f"Visualisation Grille {S}x{S}")
    plt.axis('off')
    plt.show()
