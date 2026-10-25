import skyline as sky
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Skyline GUI Showcase")

panel = sky.SkylinePanel(screen, 20, 20, 250, 230, display_frame=True, left_padding=8, right_padding=8)
label = sky.SkyLabel("Mad Ting Sad Ting")
slider1 = sky.SkySlider(10, 20, display_text=True)
slider2 = sky.SkySlider(10, 20, display_text=True)
check1 = sky.SkyCheckbox("Be Exquisite")
check2 = sky.SkyCheckbox("Be Extraordinary")

panel.add_widget(label)
panel.add_widget(slider1)
panel.add_widget(slider2)
panel.add_widget(check1)
panel.add_widget(check2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    panel.draw()
    panel.interact()
    pygame.display.update()