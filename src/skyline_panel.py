# the main panel class, central starting point
import pygame

class SkylinePanel:
    def __init__(self, screen, panel_x, panel_y, panel_width, panel_height, display_frame=True, left_padding=20, right_padding=20, main_color=(0, 22, 138), background_color=(0, 0, 0), accent_color=(44, 175, 219)):
        self.screen = screen
        self.panel_x = panel_x
        self.panel_y = panel_y
        self.panel_width = panel_width
        self.panel_height = panel_height
        self.main_color = main_color
        self.background_color = background_color
        self.accent_color = accent_color
        self.widgets = []
        self.widget_height = 0
        self.display_frame = display_frame
        self.left_padding = left_padding
        self.right_padding = right_padding

    def add_widget(self, widget):
        self.widgets.append(widget)

    def draw(self):
        self.widget_height = self.panel_height / len(self.widgets)
        for i, widget in enumerate(self.widgets):
            widget.draw(self, i)
        if self.display_frame:
            pygame.draw.rect(self.screen, self.accent_color, (self.panel_x, self.panel_y, self.panel_width, self.panel_height), width=1)

    def interact(self, pygame_keys, pygame_buttons):
        for widget in self.widgets:
            widget.interact(pygame_keys, pygame_buttons)