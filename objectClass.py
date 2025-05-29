# Perbaikan pada fungsi SAT dan struktur kode
import pygame
import math
from abc import ABC, abstractmethod

def get_axes(poly):
    axes = []
    for i in range(len(poly.points)):
        p1 = poly.points[i]
        p2 = poly.points[(i + 1) % len(poly.points)]
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
    axes1 = get_axes(poly1)
    axes2 = get_axes(poly2)
    axes = axes1 + axes2

    for axis in axes:
        min1, max1 = project_polygon(axis, poly1)
        min2, max2 = project_polygon(axis, poly2)

        # Perbaikan: pengecekan overlap harus berada dalam loop
        if max1 < min2 or max2 < min1:
            return True

    return False

class ParentObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 1
        self.angle = 0
        self.points = []
        self.update_points()

    def draw(self, screen, color):
        return pygame.draw.polygon(screen.screen, color, self.points)

    def update_points(self):
        self.points = []
        for rx, ry in self.relative_points:
            rotated_x = rx * math.cos(math.radians(self.angle)) - ry * math.sin(math.radians(self.angle))
            rotated_y = rx * math.sin(math.radians(self.angle)) + ry * math.cos(math.radians(self.angle))
            self.points.append([self.x + rx, self.y + ry])

    def movement(self, screen, dx, dy, key, collision):
        self.x += dx
        self.y += dy
        self.x = max(self.width / 2, min(self.x, screen.width - self.width / 2))
        self.y = max(self.height / 2, min(self.y, screen.height - self.height / 2))
        if collision:
            self.update_points()
        elif key[pygame.K_LEFT] or key[pygame.K_UP] or key[pygame.K_a] or key[pygame.K_w]:
            self.x += 1
            self.y += 1
            self.update_points()
        elif key[pygame.K_RIGHT] or key[pygame.K_DOWN] or key[pygame.K_d] or key[pygame.K_s]:
            self.x -= 1
            self.y -= 1
            self.update_points()
    
    def rotate(self, angle):
        self.angle = (self.angle + angle) % 360
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

    def listener(self, screen, key, collision):
        move_x, move_y = 0, 0
        if key[pygame.K_LEFT]:
            move_x -= self.velocity
        if key[pygame.K_RIGHT]:
            move_x += self.velocity
        if key[pygame.K_DOWN]:
            move_y += self.velocity
        if key[pygame.K_UP]:
            move_y -= self.velocity
        if key[pygame.K_z]:
            self.rotate(-5)  # rotasi ke kiri
        if key[pygame.K_x]:
            self.rotate(5)   # rotasi ke kanan
        if move_x != 0 or move_y != 0:
            self.movement(screen, move_x, move_y, key, collision)


class TriangleObject(ParentObject):
    def __init__(self, x, y, base, height):
        self.width = base
        self.height = height
        self.relative_points = [
            [base, -height],
            [base, height],
            [-base, height]
        ]
        super().__init__(x, y)

    def listener(self, screen, key, collision):
        move_x, move_y = 0, 0
        if key[pygame.K_a]:
            move_x -= self.velocity
        if key[pygame.K_d]:
            move_x += self.velocity
        if key[pygame.K_s]:
            move_y += self.velocity
        if key[pygame.K_w]:
            move_y -= self.velocity
        if key[pygame.K_q]:
            self.rotate(-5)  # rotasi ke kiri
        if key[pygame.K_e]:
            self.rotate(5)   # rotasi ke kanan
        if move_x != 0 or move_y != 0:
            self.movement(screen, move_x, move_y, key, collision)
