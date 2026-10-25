import pygame
from .file_loading import load_set_font

def center_text_in_rect(surface, text_surface, rect):
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def align_text_right_in_rect(surface, text_surface, rect):
    y = rect.y + (rect.height - text_surface.get_height()) / 2
    text_rect = text_surface.get_rect(right=rect.right, y=y)
    surface.blit(text_surface, text_rect)

def align_text_left_in_rect(surface, text_surface, rect):
    y = rect.y + (rect.height - text_surface.get_height()) / 2
    text_rect = text_surface.get_rect(left=rect.left, y=y)
    surface.blit(text_surface, text_rect)

def load_fitting_font(text, max_width, max_height, font_name):
    font_size = 1
    font = load_set_font(font_name, font_size)
    while True:
        w, h = font.size(text)
        if w > max_width or h > max_height:
            font_size = max(1, font_size - 1)
            return load_set_font(font_name, font_size)
        font_size += 1
        font = load_set_font(font_name, font_size)

def truncate_pygame_text(text, font_size, max_width, font_name):
    if len(text) < 2:
        raise ValueError("The text string is too short.")
    truncated_text = None
    font = load_set_font(font_name, font_size)
    text_surface = font.render(text, True, (0,0,0))
    if text_surface.get_width() <= max_width:
        return text
    else:
        shortened_text = text[:-1]
        truncated_text = f"{shortened_text}..."
        text_surface = font.render(truncated_text, True, (0, 0, 0))
        while text_surface.get_width() > max_width:
            shortened_text = shortened_text[:-1]
            truncated_text = f"{shortened_text}..."
            text_surface = font.render(truncated_text, True, (0, 0, 0))
    return truncated_text