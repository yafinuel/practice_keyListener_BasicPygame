import pygame

class Screen:
    def __init__(self, width, height, bgColor):
        self.bgColor = bgColor
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Latihan game sederhana")
    
    def fill(self):
        return self.screen.fill(self.bgColor)