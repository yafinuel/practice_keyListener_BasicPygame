import pygame
from abc import ABC, abstractmethod

class ParentObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 1
    
    def listener(self, screen, key):
        move_x, move_y = 0, 0
        if key[pygame.K_LEFT]:
            move_x -= self.velocity
            self.movement(screen, move_x, move_y)
        if key[pygame.K_RIGHT]:
            move_x += self.velocity
            self.movement(screen, move_x, move_y)
        if key[pygame.K_DOWN]:
            move_y += self.velocity
            self.movement(screen, move_x, move_y)
        if key[pygame.K_UP]:
            move_y -= self.velocity
            self.movement(screen, move_x, move_y)
        if key[pygame.K_q]:
            self.rotate(screen.screen)

    def draw(self, screen, color):
        return pygame.draw.polygon(screen.screen, color, self.points)


class ColObject(ParentObject):

    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.object = pygame.Rect(x, y, width, height)
    
    def draw(self, screen, color):
        return pygame.draw.rect(screen, color, self.object)
    
    def movement(self, screen, x, y):
        self.object = self.object.move(x, y)
        self.object.x = max(0, min(self.object.x, screen.width - self.object.width))
        self.object.y = max(0, min(self.object.y, screen.height - self.object.height))
        return self.object
    
    def rotate(self):
        pass

class RectObject(ParentObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

        self.relative_points = [
            [-width/2, -height/2],
            [width/2, -height/2], 
            [width/2, height/2], 
            [-width/2, height/2]
        ]
        self.points = []
        self.update_points()
    
    def update_points(self):
        self.points = []
        for rx, ry in self.relative_points:
            self.points.append([self.x + rx, self.y + ry])
    
    def movement(self, screen, dx, dy):
        self.x += dx
        self.y += dy

        self.x = max(self.width/2, min(self.x, screen.width - self.width/2))
        self.y = max(self.height/2, min(self.y, screen.height - self.height/2))

        self.update_points()

class TriangleObject(ParentObject):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.width = base
        self.height = height

        self.relative_points = [
            [base, -height],
            [base, height], 
            [-base, height]
        ]
        self.points = []
        self.update_points()
    
    def update_points(self):
        self.points = []
        for rx, ry in self.relative_points:
            self.points.append([self.x + rx, self.y + ry])
    
    def movement(self, screen, dx, dy):
        self.x += dx
        self.y += dy

        self.x = max(self.width/2, min(self.x, screen.width - self.width/2))
        self.y = max(self.height/2, min(self.y, screen.height - self.height/2))

        self.update_points()

    def listener(self, screen, key):
        move_x, move_y = 0, 0
        if key[pygame.K_a]:
            move_x -= self.velocity
            self.movement(screen, move_x, move_y)
        if key[pygame.K_d]:
            move_x += self.velocity
            self.movement(screen, move_x, move_y)
        if key[pygame.K_s]:
            move_y += self.velocity
            self.movement(screen, move_x, move_y)
        if key[pygame.K_w]:
            move_y -= self.velocity
            self.movement(screen, move_x, move_y)
        if key[pygame.K_q]:
            self.rotate(screen.screen)
    


