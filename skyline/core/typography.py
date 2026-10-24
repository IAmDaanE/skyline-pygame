import pygame
from ..utils import load_pygame_font

def center_text_in_rect(surface, text_surface, rect):
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def align_text_right_in_rect(surface, text_surface, rect):
    y = rect.y + (rect.height - text_surface.get_height()) / 2
    text_rect = text_surface.get_rect(right=rect.right, y=y)
    surface.blit(text_surface, text_rect)

def load_fitting_font(text, max_width, max_height, font_name):
    font_size = 1
    font = load_pygame_font(font_name, font_size)
    while True:
        w, h = font.size(text)
        if w > max_width or h > max_height:
            font_size = max(1, font_size - 1)
            return load_pygame_font(font_name, font_size)
        font_size += 1
        font = load_pygame_font(font_name, font_size)