import pygame
import sys

# Inisialisasi Pygame
pygame.init()
font = pygame.font.SysFont(None, 48)

# Screen build
screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Menggerakkan Objek")

# Color defines
bgColor = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)

size = 50
speed = 1
# Make objek
objek1 = pygame.Rect(0, screen_h // 2 - size // 2, size, size)
objek2 = pygame.Rect(screen_w - size, screen_h // 2 - size // 2, size, size)
teks = font.render("Tabrakan", True, (255,255,255))
teks_rect = teks.get_rect(center=(300,200))

running = True
while running:
	move_x1, move_y1 = 0, 0
	move_x2, move_y2 = 0,0
	
	screen.fill(bgColor)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	# RENDER YOUR GAME HERE
	prev_objek1 = objek1.copy()
	prev_objek2 = objek2.copy()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		move_x1 -= speed
	if keys[pygame.K_RIGHT]:
		move_x1 += speed
	if keys[pygame.K_DOWN]:
		move_y1 += speed
	if keys[pygame.K_UP]:
		move_y1 -= speed
	if keys[pygame.K_a]:
		move_x2 -= speed
	if keys[pygame.K_d]:
		move_x2 += speed
	if keys[pygame.K_s]:
		move_y2 += speed
	if keys[pygame.K_w]:
		move_y2 -= speed

	objek1 = objek1.move(move_x1, move_y1)
	objek2 = objek2.move(move_x2, move_y2)


	objek1.x = max(0, min(objek1.x, screen_w - size))
	objek1.y = max(0, min(objek1.y, screen_h - size))
	objek2.x = max(0, min(objek2.x, screen_w - size))
	objek2.y = max(0, min(objek2.y, screen_h - size))

	pygame.draw.rect(screen, red, objek1)
	pygame.draw.rect(screen, green, objek2)
	
	if objek1.colliderect(objek2):
		objek1 = prev_objek1
		objek2 = prev_objek2
		screen.blit(teks, teks_rect)

	# flip() the display to put your work on screen
	pygame.display.flip()

pygame.quit()
sys.exit()