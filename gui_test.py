import skyline as sky
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Skyline GUI Showcase")

panel = sky.SkylinePanel(screen, 800 - 320, 20, 300, 560, display_frame=True, )
label = sky.SkyLabel("Mad Ting Yea")

panel.add_widget(label)

running = True

while running:
    for event in pygame.events.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    panel.draw()
    pygame.display.update()