import pygame

def center_text_in_rect(screen, text_surface, rect):
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)