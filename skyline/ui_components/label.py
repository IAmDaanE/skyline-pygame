import pygame
from ..core.typography import center_text_in_rect

class SkyLabel:
    def __init__(self, text_string=None, font="JetBrainsMono-Regular", background_color=None, text_color=None, centered=True):
        self.text_string = text_string
        self.font = font
        self.background_color = background_color
        self.text_color = text_color
        self.centered = centered

    def draw(self, panel_class, index):
        if self.background_color == None:
            self.background_color = panel_class.background_color
        if self.text_color == None:
            self.text_color = panel_class.accent_color
        rect = None

    def interact(self, pygame_keys, pygame_buttons, pygame_mouse_pos):
        pass # permanent, a label is static