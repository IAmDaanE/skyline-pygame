import pygame
from ..utils import load_pygame_font

def center_text_in_rect(screen, text_surface, rect):
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def get_font_size(text, max_width, max_height, font_name):
    font_size = 1
    font = load_pygame_font(font_name, font_size)
    
    while True:
        w, h = font.size(text)
        if w > max_width or h > max_height:
            font_size = max(1, font_size - 1)
            return load_pygame_font(font_name, font_size)
        font_size += 1
        font = load_pygame_font(font_name, font_size)