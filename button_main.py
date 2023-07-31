import pygame
import button

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

print("button_main.py run")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blimp Base Station")

#load button images
left_arrow_img = pygame.image.load('left_arrow.png').convert_alpha()
up_arrow_img = pygame.image.load('up_arrow.png').convert_alpha()
right_arrow_img = pygame.image.load('right_arrow.png').convert_alpha()
down_arrow_img = pygame.image.load('down_arrow.png').convert_alpha()

#create button instances
left_arrow = button.Button(100, 200, left_arrow_img, 1)
forward_arrow = button.Button(200, 200, up_arrow_img, 1)
right_arrow = button.Button(300, 200, right_arrow_img, 1)
up_arrow = button.Button(500, 200, up_arrow_img, 1)
down_arrow = button.Button(500, 300, down_arrow_img, 1)

def send_directions(direction, conn):
    if direction == "left":
        conn.sendall(str.encode("left"))
    elif direction == "right":
        conn.sendall(str.encode("right"))
    elif direction == "forward":
        conn.sendall(str.encode("forward"))
    elif direction == "up":
        conn.sendall(str.encode("up"))
    elif direction == "down":
        conn.sendall(str.encode("down"))

#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	if left_arrow.draw(screen):
		print('LEFT')
		send_directions(direction, conn)
	if right_arrow.draw(screen):
		print('RIGHT')
	if forward_arrow.draw(screen):
		print('FORWARD')
	# if up_arrow.draw(screen):
	# 	print('UP')
	# if down_arrow.draw(screen):
	# 	print('DOWN')

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()