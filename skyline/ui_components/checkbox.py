import pygame 
from ..core.typography import load_fitting_font, align_text_right_in_rect, truncate_pygame_text, align_text_left_in_rect
from ..core.image_processing import load_and_replace_image_colors
from ..core.file_loading import load_set_font

class SkyCheckbox:
    def __init__(self, text_string, background_color=None, checkbox_color=None, checkmark_color=None, text_color=None, font_name=None, enabled=False, vertical_text_gap=5, box_text_spacing=8, checkbox_size=16, font_size=None, dynamic_font_size=False, left_padding=None, right_padding=None):
        self.text_string = text_string
        self.background_color = background_color
        self.checkbox_color = checkbox_color
        self.checkmark_color = checkmark_color
        self.text_color = text_color
        self.font_name = font_name
        self.enabled = enabled
        self.checkbox_rect = None
        self.global_checkbox_rect = None
        self.big_text_rect = None
        self.vertical_text_gap = vertical_text_gap
        self.box_text_spacing = box_text_spacing
        self.font = None
        self.text = None
        self.checkbox_size = checkbox_size
        self.checkmark_image = None
        self.clicked_prev_frame = False
        self.font_size = font_size
        self.dynamic_font_size = dynamic_font_size
        self.left_padding = left_padding
        self.right_padding = right_padding

    def setup(self, panel_class, index):
        if self.background_color == None:
            self.background_color = panel_class.background_color
        if self.checkbox_color == None:
            self.checkbox_color = panel_class.accent_color
        if self.checkmark_color == None:
            self.checkmark_color = panel_class.main_color
        if self.text_color == None:
            self.text_color = panel_class.main_color
        if self.font_name == None:
            self.font_name = panel_class.font_name
        if self.checkbox_rect == None:
                self.checkbox_rect = pygame.Rect(panel_class.left_padding, panel_class.widget_height / 2 - self.checkbox_size / 2, self.checkbox_size, self.checkbox_size)
        if self.big_text_rect == None:
                self.big_text_rect = pygame.Rect(self.checkbox_rect.right + self.box_text_spacing, self.vertical_text_gap, panel_class.panel_width - panel_class.left_padding - panel_class.right_padding - self.box_text_spacing - self.checkbox_rect.width, panel_class.widget_height - 2 * self.vertical_text_gap)
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
        if self.checkmark_image == None:
                self.checkmark_image = load_and_replace_image_colors("checkmark", (0, 0, 0), self.checkmark_color)

    def interact(self, pygame_keys, pygame_buttons, pygame_mouse_pos):
        if pygame_buttons[0]:
            if self.global_checkbox_rect.collidepoint(pygame_mouse_pos):
                if not self.clicked_prev_frame:
                    self.enabled = not self.enabled
            self.clicked_prev_frame = True
        else:
            self.clicked_prev_frame = False

    def draw(self, panel_class, widget_surface, index):
        widget_surface.fill(self.background_color)
        widget_height = int(widget_surface.get_height())
        widget_width = int(widget_surface.get_width())
        self.global_checkbox_rect = pygame.Rect(self.checkbox_rect.x + panel_class.panel_x, widget_height * index + self.checkbox_rect.y + panel_class.panel_y, self.checkbox_size, self.checkbox_size)
        align_text_left_in_rect(widget_surface, self.text, self.big_text_rect)
        pygame.draw.rect(widget_surface, self.checkbox_color, self.checkbox_rect, border_radius=3)
        if self.enabled:
            widget_surface.blit(self.checkmark_image, self.checkbox_rect)
        #pygame.draw.rect(widget_surface, (255, 0, 0), self.big_text_rect, width=1)
        #pygame.draw.rect(panel_class.screen, (255, 0, 0), self.global_checkbox_rect, width=1)

    def get_value(self):
            return self.enabled