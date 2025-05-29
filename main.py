import pygame
import sys
from screenclass import Screen
from objectClass import RectObject, TriangleObject, polygons_collide

pygame.init()

screen = Screen(500,500, "white")
mainObj = RectObject(50, 50,50,50)
triObj = TriangleObject(350, 50, 50, 50)

running = True
while running:
    screen.fill()
    pygame.time.delay(2)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()	
    mainObj.listener(screen, keys, polygons_collide(mainObj, triObj))
    triObj.listener(screen, keys, polygons_collide(triObj, mainObj))

    # Drawing
    mainObj.draw(screen, "red")
    triObj.draw(screen, "green")
    
    

    pygame.display.flip()


pygame.quit()
sys.exit()