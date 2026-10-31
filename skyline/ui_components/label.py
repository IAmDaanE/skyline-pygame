import pygame
from ..core.typography import center_text_in_rect, load_fitting_font, align_text_left_in_rect, align_text_right_in_rect, truncate_pygame_text
from ..core.file_loading import load_set_font

class SkyLabel:
    def __init__(self, text_string, font_name=None, background_color=None, text_color=None, vertical_gap=5, font_size=None, dynamic_font_size=False):
        self.text_string = text_string
        self.font_name = font_name
        self.background_color = background_color
        self.text_color = text_color
        self.vertical_gap = vertical_gap
        self.font = None
        self.font_size = font_size
        self.dynamic_font_size = dynamic_font_size
        self.text = None
        self.big_text_rect = None

    def setup(self, panel_class, index):
        if self.background_color == None:
            self.background_color = panel_class.background_color
        if self.text_color == None:
            self.text_color = panel_class.accent_color
        if self.big_text_rect == None:
            full_rect = pygame.Rect(panel_class.panel_x, panel_class.panel_y, panel_class.panel_width, panel_class.widget_height)
            self.big_text_rect = pygame.Rect(panel_class.left_padding, self.vertical_gap, full_rect.width - panel_class.left_padding - panel_class.right_padding, full_rect.height - 2 * self.vertical_gap)
        if self.font_name == None:
            self.font_name = panel_class.font_name
        if self.font_size == None:
            if self.dynamic_font_size:
                self.font = self.font = load_fitting_font(self.text_string, self.big_text_rect.width, self.big_text_rect.height, self.font_name)
            else:
                self.font_size = panel_class.font_size
        if self.font == None:
            self.font = load_set_font(self.font_name, self.font_size)
        if self.text == None:
            if not self.dynamic_font_size:
                self.text_string = truncate_pygame_text(self.text_string, self.font_size, self.big_text_rect.width, self.font_name)
            self.text = self.font.render(self.text_string, True, self.text_color)

    def draw(self, panel_class, widget_surface, index):
        widget_surface.fill(self.background_color)
        center_text_in_rect(widget_surface, self.text, self.big_text_rect)

    def interact(self, pygame_keys, pygame_buttons, pygame_mouse_pos):
        pass # permanent, a label is static