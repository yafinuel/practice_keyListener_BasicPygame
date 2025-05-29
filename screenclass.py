import pygame

class Screen:
    def __init__(self, width, height, bg_color):
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Latihan Game Sederhana")

    def fill(self):
        self.screen.fill(self.bg_color)