import skyline as sky
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Skyline GUI Showcase")

panel = sky.SkylinePanel(screen, 20, 20, 90, 60, display_frame=True, left_padding=6, right_padding=6)
label1 = sky.SkyLabel("Mad Ting Yea")
label2 = sky.SkyLabel("Big Man Ting")

panel.add_widget(label1)
panel.add_widget(label2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    panel.draw()
    pygame.display.update()