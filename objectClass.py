import pygame
import math
from abc import ABC, abstractmethod
clock = pygame.time.Clock()


def get_axes(polygon):
    axes = []
    for i in range(len(polygon.points)):
        p1 = polygon.points[i]
        p2 = polygon.points[(i + 1) % len(polygon.points)]
        edge = (p2[0] - p1[0], p2[1] - p1[1])
        normal = (-edge[1], edge[0])
        length = math.hypot(normal[0], normal[1])
        if length != 0:
            axes.append((normal[0] / length, normal[1] / length))
    return axes

def project_polygon(axis, polygon):
    dots = [point[0] * axis[0] + point[1] * axis[1] for point in polygon.points]
    return min(dots), max(dots)

def polygons_collide(poly1, poly2):
    axes = get_axes(poly1) + get_axes(poly2)
    for axis in axes:
        min1, max1 = project_polygon(axis, poly1)
        min2, max2 = project_polygon(axis, poly2)
        if max1 < min2 or max2 < min1:
            return False
    return True

class ParentObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 2
        self.points = []
        self.angle = 0
        self.update_points()

    def update_points(self):
        cos_a = math.cos(math.radians(self.angle))
        sin_a = math.sin(math.radians(self.angle))
        self.points = []
        for rx, ry in self.relative_points:
            rotated_x = rx * cos_a - ry * sin_a
            rotated_y = rx * sin_a + ry * cos_a
            self.points.append([self.x + rotated_x, self.y + rotated_y])

    def draw(self, screen, color):
        pygame.draw.polygon(screen.screen, color, self.points)

    def move(self, dx, dy, screen):
        self.x = max(self.width / 2, min(self.x + dx, screen.width - self.width / 2))
        self.y = max(self.height / 2, min(self.y + dy, screen.height - self.height / 2))
        self.update_points()

    def rotate(self, da):
        self.angle = (self.angle + da) % 360
        self.update_points()
    
    def mirror_x(self):
        for i in range(len(self.relative_points)):
            self.relative_points[i][0] *= -1
        self.update_points()
    
    def mirror_y(self):
        for i in range(len(self.relative_points)):
            self.relative_points[i][1] *= -1
        self.update_points()

class RectObject(ParentObject):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.relative_points = [
            [-width / 2, -height / 2],
            [width / 2, -height / 2],
            [width / 2, height / 2],
            [-width / 2, height / 2]
        ]
        super().__init__(x, y)

    def listener(self, keys, screen):
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.velocity
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * self.velocity
        if keys[pygame.K_q]:
            self.rotate(-5)
        if keys[pygame.K_e]:
            self.rotate(5)
        self.move(dx, dy, screen)

class TriangleObject(ParentObject):
    def __init__(self, x, y, base, height):
        self.width = base
        self.height = height
        self.relative_points = [
            [0, -height / 2],
            [base / 2, height / 2],
            [-base / 2, height / 2]
        ]
        super().__init__(x, y)

    def listener(self, keys, screen):
        dx = (keys[pygame.K_d] - keys[pygame.K_a]) * self.velocity
        dy = (keys[pygame.K_s] - keys[pygame.K_w]) * self.velocity
        if keys[pygame.K_z]:
            self.rotate(-5)
        if keys[pygame.K_c]:
            self.rotate(5)
        if keys[pygame.K_m]:
            self.mirror_x()
        if keys[pygame.K_n]:
            self.mirror_y()
        self.move(dx, dy, screen)
