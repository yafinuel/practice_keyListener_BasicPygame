import pygame
import sys
pygame.init()

class Screen:
    def __init__(self, width, height, bgColor):
        self.bgColor = bgColor
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Latihan game sederhana")
    
    def fill(self):
        return self.screen.fill(self.bgColor)

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
            self.scale()
        
        
    def movement(self, screen, x, y):
        self.object = self.object.move(x, y)
        self.object.x = max(0, min(self.object.x, screen.width - self.object.width))
        self.object.y = max(0, min(self.object.y, screen.height - self.object.height))
        return self.object
    
    def scale(self):
        self.object.width += 1
        self.object.height += 1


class RectObject(ParentObject):

    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.object = pygame.Rect(x, y, width, height)  
    
    def draw(self, screen, color):
        return pygame.draw.rect(screen, color, self.object)


screen = Screen(500,500, "white")
firstObj = RectObject(0,0,50,50)
secObj = RectObject(250-50,screen.height-200,100,200)

running = True
while running:
    screen.fill()
    pygame.time.delay(2)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Collisions
    colObj = firstObj.object

    # Movement
    keys = pygame.key.get_pressed()	
    firstObj.listener(screen, keys)

    # Drawing
    firstObj.draw(screen.screen, "red")
    secObj.draw(screen.screen, "blue")

    # Collisions
    if firstObj.object.colliderect(secObj.object):
        firstObj.object = colObj


    pygame.display.flip()


pygame.quit()
sys.exit()