import pygame
import sys
import random

pygame.init()

score = 0
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")
player = pygame.Rect(300, 300, 25, 25)  # Create a rectangle for the player
apple = pygame.Rect(100,100,25,25)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 10
    if keys[pygame.K_d]:
        player.x += 10
    if keys[pygame.K_w]:
        player.y -= 10
    if keys[pygame.K_s]:
        player.y += 10

    screen.fill((255, 255, 255))  # Fill the screen with white
    pygame.draw.rect(screen, ("yellow"), player)  # Draw the player rectangle
    pygame.draw.rect(screen, (255, 0, 0), apple)
    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS

    if player.colliderect(apple):
        score += 1
        print(score)
        apple.x = random.randint(0, 775)
        apple.y = random.randint(0, 575)




pygame.quit()
sys.exit()