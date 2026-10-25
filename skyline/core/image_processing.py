from PIL import Image
import pygame
import numpy as np
from .file_loading import load_image

def pillow_to_pygame(pil_image):
    if pil_image.mode not in ("RGB", "RGBA"):
        pil_image = pil_image.convert("RGBA")
    mode = pil_image.mode
    size = pil_image.size
    raw_data = pil_image.tobytes()
    surface = pygame.image.frombuffer(raw_data, size, mode)
    if mode == "RGBA":
        return surface.convert_alpha()
    else:
        return surface.convert()

def load_and_replace_image_colors(image_name, current_rgb, goal_rgb):
    pil_img = load_image(image_name).convert("RGBA")
    arr = np.array(pil_img)
    rgb = arr[:, :, :3]
    mask = np.all(rgb == current_rgb, axis=-1)
    arr[mask, :3] = goal_rgb
    return pillow_to_pygame(Image.fromarray(arr))