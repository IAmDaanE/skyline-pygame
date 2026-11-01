from skyline import SkylinePanel, SkyLabel, SkySlider, SkyCheckbox
import pygame

WINDOW_WIDTH = 680
WINDOW_HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Skyline GUI Showcase")
running = True

ball_x = 0
ball_y = 0
ball_size = 0

panel1 = SkylinePanel(screen, 20, 20, 200, 360, display_frame=True, display_separations=True, left_padding=8, right_padding=8, background_color=(255, 255, 255))
ball_controls_label = SkyLabel("Ball Controls")
size_slider = SkySlider(10, 60, display_text=True)
y_slider = SkySlider(50, 350, display_text=True)
x_slider = SkySlider(250, 430, display_text=True)
colorful_ball_checkbox = SkyCheckbox("Colorful Ball", font_size=16)
panel1.add_widget(ball_controls_label)
panel1.add_widget(size_slider)
panel1.add_widget(x_slider)
panel1.add_widget(y_slider)
panel1.add_widget(colorful_ball_checkbox)

panel2 = SkylinePanel(screen, 460, 20, 200, 360, display_frame=True, display_separations=True, left_padding=8, right_padding=8, background_color=(255, 255, 255))
panel2.add_widget(SkyLabel("Anaheim", font_name="Anaheim-Regular"))
panel2.add_widget(SkyLabel("BebasNeue", font_name="BebasNeue-Regular"))
panel2.add_widget(SkyLabel("Exo", font_name="Exo-Regular"))
panel2.add_widget(SkyLabel("GeistPixel", font_name="GeistPixel-Regular"))
panel2.add_widget(SkyLabel("LiberationSans", font_name="LiberationSans-Regular"))
panel2.add_widget(SkyLabel("PlayfairDisplay", font_name="PlayfairDisplay-Regular"))
panel2.add_widget(SkyLabel("RubikBrokenFax", font_name="RubikBrokenFax-Regular"))
panel2.add_widget(SkyLabel("Righteous", font_name="Righteous-Regular"))
panel2.add_widget(SkyLabel("Saira", font_name="Saira-Regular"))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # interacting
    panel1.interact()
    ball_x = x_slider.get_value()
    ball_y = y_slider.get_value()
    ball_size = size_slider.get_value()
    colorful_ball = colorful_ball_checkbox.get_value()
    
    panel2.interact()

    # displaying
    screen.fill((0, 0, 0))
    panel1.draw()
    if colorful_ball:
        pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_size / 2)
    else:
        pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_size / 2)
    panel2.draw()
    pygame.display.update()