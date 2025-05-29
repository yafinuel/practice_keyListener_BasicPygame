import pygame
import sys
from screenclass import Screen
from objectClass import RectObject, TriangleObject, polygons_collide

pygame.init()

screen = Screen(500, 500, (255, 255, 255))
rect = RectObject(100, 100, 60, 60)
triangle = TriangleObject(300, 300, 80, 80)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    screen.fill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    prev_rect = rect.x, rect.y, rect.angle
    prev_triangle = triangle.x, triangle.y, triangle.angle

    rect.listener(keys, screen)
    triangle.listener(keys, screen)

    if polygons_collide(rect, triangle):
        rect.x, rect.y, rect.angle = prev_rect
        triangle.x, triangle.y, triangle.angle = prev_triangle
        rect.update_points()
        triangle.update_points()

    rect.draw(screen, (255, 0, 0))
    triangle.draw(screen, (0, 255, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()
