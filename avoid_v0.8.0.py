'''
ELLAK - Python Course
Avoid the Rocks v0.8.0
 
'''
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 600)
spaceship_size = (40,40)
screen = pygame.display.set_mode(size)

# Load the background image 
background_image = pygame.image.load("background.jpg").convert()


spaceshipImg = pygame.image.load("spaceship.png")
meteorImg    = pygame.image.load("meteor.png")
 
pygame.display.set_caption("ELLAK - Pyhton Course - Avoid The Rocks v0.8.0")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

ship_x = 500
ship_y = 380
ship_x_speed = 0
ship_y_speed = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    ship_x_speed = 5
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    ship_x_speed = -5
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    ship_y_speed = 5
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    ship_y_speed = -5

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    ship_x_speed = 0
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    ship_x_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ship_y_speed = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    ship_y_speed = 0
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    #screen.fill(GREY)
    screen.blit(background_image, [0, 0])
 
    # --- Drawing code should go here
    
    screen.blit(spaceshipImg, (ship_x, ship_y))
    if ship_x >= 0 and ship_x <= size[0]-spaceship_size[0]:
        ship_x += ship_x_speed
    elif ship_x < 0:
        ship_x = 1
        ship_x_speed = 0
    elif ship_x > size[0]-spaceship_size[0]:
        ship_x = size[0]-spaceship_size[0]
        ship_x_speed = 0
    if ship_y >= 0 and ship_y <= size[1]-spaceship_size[1]:
        ship_y += ship_y_speed
    elif ship_y < 0:
        ship_y = 1
        ship_y_speed = 0
    elif ship_y > size[1]-spaceship_size[1]:
        ship_y = size[1]-spaceship_size[1]
        ship_y_speed = 0
    print(ship_x, ship_y)
    
        
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
