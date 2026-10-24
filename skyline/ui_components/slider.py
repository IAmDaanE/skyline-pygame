import pygame
from ..core.typography import load_fitting_font, center_text_in_rect, align_text_right_in_rect
from ..utils import round_to_num_digits

class SkySlider:
    def __init__(self, min_value, max_value, background_color=None, slide_path_color=None, slide_grip_color=None, text_color=None, display_text=False, font_name="JetBrainsMono-Regular", rounded_digits=3):
        if max_value < min_value or max_value == min_value:
            raise ValueError("Max value should be higher then min value.")
        self.min_value = min_value
        self.max_value = max_value
        self.background_color = background_color
        self.slide_path_color = slide_path_color
        self.slide_grip_color = slide_grip_color
        self.text_color = text_color
        self.value = min_value + (max_value - min_value) / 2
        self.local_grip_rect = None
        self.display_text = display_text
        self.sliding_path_rect = None
        self.big_text_rect = None
        self.font = None
        self.font_name = font_name
        self.prev_x = None
        self.x_step = None
        self.global_grip_rect = None
        self.rounded_digits = rounded_digits
        self.dragging = False

    def interact(self, pygame_keys, pygame_buttons, pygame_mouse_pos):
        if pygame_buttons[0]:
            if self.dragging:
                x_plus = pygame_mouse_pos[0] - self.prev_x
                self.local_grip_rect.x += x_plus
                self.local_grip_rect.x = max(self.sliding_path_rect.left, min(self.local_grip_rect.x, self.sliding_path_rect.right - self.local_grip_rect.width))
                travel = self.sliding_path_rect.width - self.local_grip_rect.width
                if travel > 0:
                    progress = (self.local_grip_rect.x - self.sliding_path_rect.left) / travel
                    self.value = self.min_value + progress * (self.max_value - self.min_value)
                self.prev_x = pygame_mouse_pos[0]
            elif self.global_grip_rect.collidepoint(pygame_mouse_pos):
                self.prev_x = pygame_mouse_pos[0]
                self.dragging = True
        else:
            self.prev_x = None
            self.dragging = False
        
    def draw(self, panel_class, widget_surface, index):
        if self.background_color == None:
            self.background_color = panel_class.background_color
        if self.slide_path_color == None:
            self.slide_path_color = panel_class.main_color
        if self.slide_grip_color == None:
            self.slide_grip_color = panel_class.accent_color
        if self.text_color == None:
            self.text_color = panel_class.accent_color
        sliding_path_height = 8
        sliding_path_text_gap = 20
        widget_height = int(widget_surface.get_height())
        widget_width = int(widget_surface.get_width())
        if self.sliding_path_rect == None:
            if not self.display_text:
                self.sliding_path_rect = pygame.Rect(panel_class.left_padding, widget_height / 2 - sliding_path_height / 2, widget_width - panel_class.left_padding - panel_class.right_padding, sliding_path_height)
            else:
                self.sliding_path_rect = pygame.Rect(panel_class.left_padding, widget_height / 2 - sliding_path_height / 2, (widget_width - panel_class.left_padding - panel_class.right_padding) * 0.85 - sliding_path_text_gap / 2, sliding_path_height)
        if self.x_step == None:
            self.x_step = (self.max_value - self.min_value) / self.sliding_path_rect.width
        grip_width = 8
        grip_height = 20
        if self.local_grip_rect == None:
            self.local_grip_rect = pygame.Rect(self.sliding_path_rect.x + self.x_step * (self.value - self.min_value), panel_class.widget_height / 2 - grip_height / 2, grip_width, grip_height)
        else:
            self.global_grip_rect = pygame.Rect(self.local_grip_rect.x + panel_class.panel_x, self.local_grip_rect.y + panel_class.panel_y + int(widget_surface.get_height()) * index, self.local_grip_rect.width, self.local_grip_rect.height)
        if self.display_text and self.big_text_rect == None:
            self.big_text_rect = pygame.Rect(self.sliding_path_rect.right + sliding_path_text_gap / 2, 5, (widget_width - panel_class.left_padding - panel_class.right_padding) * 0.15, widget_height - 10)
        if self.font == None and self.display_text:
            self.font = load_fitting_font(str(round_to_num_digits(self.value, self.rounded_digits)), self.big_text_rect.width, self.big_text_rect.height, self.font_name)
        if self.display_text:
            text = self.font.render(str(round_to_num_digits(self.value, self.rounded_digits)), True, self.text_color)
            align_text_right_in_rect(widget_surface, text, self.big_text_rect)
        pygame.draw.rect(widget_surface, panel_class.main_color, self.sliding_path_rect)
        pygame.draw.rect(widget_surface, panel_class.accent_color, self.local_grip_rect)
        #pygame.draw.rect(widget_surface, (255, 0, 0), self.big_text_rect, width=1)
        #pygame.draw.rect(widget_surface, (255, 0, 0), self.sliding_path_rect, width=1)
        
    def get_value(self):
        return self.value