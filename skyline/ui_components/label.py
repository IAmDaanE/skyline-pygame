import pygame
from ..core.typography import center_text_in_rect, load_fitting_font
from ..core.file_loading import load_set_font

class SkyLabel:
    def __init__(self, text_string, font_name="JetBrainsMono-Regular", background_color=None, text_color=None, vertical_gap=5):
        self.text_string = text_string
        self.font_name = font_name
        self.background_color = background_color
        self.text_color = text_color
        self.vertical_gap = vertical_gap
        self.font = None

    def draw(self, panel_class, widget_surface, index):
        if self.background_color == None:
            self.background_color = panel_class.background_color
        if self.text_color == None:
            self.text_color = panel_class.accent_color
        full_rect = widget_surface.get_rect()
        smaller_rect = pygame.Rect(panel_class.left_padding, self.vertical_gap, full_rect.width - panel_class.left_padding - panel_class.right_padding, full_rect.height - 2 * self.vertical_gap)
        if self.font == None:
            self.font = load_fitting_font(self.text_string, smaller_rect.width, smaller_rect.height, self.font_name)
        text = self.font.render(self.text_string, True, self.text_color)
        widget_surface.fill(self.background_color)
        center_text_in_rect(widget_surface, text, smaller_rect)

    def interact(self, pygame_keys, pygame_buttons, pygame_mouse_pos):
        pass # permanent, a label is static