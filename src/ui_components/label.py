import pygame

class SkyLabel:
    def __init__(self, text_string=None, font="JetBrainsMono-Regular", background_color=None, text_color=None, centered=True):
        self.text_string = text_string
        self.font = font
        self.background_color = background_color
        self.text_color = text_color
        self.centered = centered

    def draw(self, panel_class, index):
        y = 

    def interact(self, pygame_keys, pygame_buttons):
        pass # permanent, a label is static