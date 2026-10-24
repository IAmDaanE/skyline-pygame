import skyline as sky
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Skyline GUI Showcase")

panel = sky.SkylinePanel(screen, 20, 20, 250, 100, display_frame=True, left_padding=8, right_padding=8)
label = sky.SkyLabel("Mad Ting Yea")
slider1 = sky.SkySlider(10, 20, display_text=True)
slider2 = sky.SkySlider(10, 20, display_text=True)

panel.add_widget(label)
panel.add_widget(slider1)
panel.add_widget(slider2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    panel.draw()
    panel.interact()
    pygame.display.update()