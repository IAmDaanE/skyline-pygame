import pygame
import io
from importlib import resources
from PIL import Image

def load_set_font(font_name, font_size):
    asset_path = resources.files("skyline").joinpath(f"assets/fonts/{font_name}.ttf")
    font_bytes = asset_path.read_bytes()    
    font_stream = io.BytesIO(font_bytes)
    return pygame.font.Font(font_stream, font_size)

def load_image(image_name):
    asset_path = resources.files("skyline").joinpath(f"assets/images/{image_name}.png")
    image_bytes = asset_path.read_bytes()
    image_stream = io.BytesIO(image_bytes)
    return Image.open(image_stream)