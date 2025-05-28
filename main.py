import pygame
import sys
from screenclass import Screen
from objectClass import ColObject, RectObject, TriangleObject

pygame.init()

screen = Screen(500,500, "white")
mainObj = RectObject(50, 50,50,50)
triObj = TriangleObject(350, 50, 50, 50)
propObj = ColObject(250-50,screen.height-200,100,200)

running = True
while running:
    screen.fill()
    pygame.time.delay(2)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()	
    mainObj.listener(screen, keys)
    triObj.listener(screen, keys)

    # Drawing
    propObj.draw(screen.screen, "blue")
    mainObj.draw(screen, "red")
    triObj.draw(screen, "green")

    pygame.display.flip()


pygame.quit()
sys.exit()