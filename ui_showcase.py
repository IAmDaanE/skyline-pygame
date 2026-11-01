import skyline as sky
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Skyline GUI Showcase")

panel = sky.SkylinePanel(screen, 20, 20, 250, 230, display_frame=True, display_separations=True, left_padding=8, right_padding=8, background_color=(255, 255, 255))
label = sky.SkyLabel("Mad Ting Sad Ting", dynamic_font_size=True)
slider1 = sky.SkySlider(10, 20, display_text=True)
slider2 = sky.SkySlider(10, 20, display_text=True)
check1 = sky.SkyCheckbox("Be Exquisite", dynamic_font_size=False)
check2 = sky.SkyCheckbox("Be Extraordinary", dynamic_font_size=False, left_padding=24)

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