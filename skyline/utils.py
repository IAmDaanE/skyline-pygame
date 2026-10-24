import pygame
from importlib import resources
import io

def load_pygame_font(font_filename, font_size):
    asset_path = resources.files("skyline").joinpath(f"assets/fonts/{font_filename}.ttf")
    font_bytes = asset_path.read_bytes()    
    font_stream = io.BytesIO(font_bytes)
    return pygame.font.Font(font_stream, font_size)

def round_to_num_digits(value, max_digits):
    integer_digits = len(str(abs(int(value))))
    decimal_places = max_digits - integer_digits
    if decimal_places <= 0:
        return int(value)
    return round(value, decimal_places)