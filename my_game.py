import pygame
import sys
import random

pygame.init()

score = 0
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")
player = pygame.Rect(300, 300, 25, 25)  # Create a rectangle for the player
apple = pygame.Rect(100,100,20,20)
square = pygame.Rect(200,200,25,25)
enemy_delay = 5000
start_time = pygame.time.get_ticks()

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

    player.clamp_ip(screen.get_rect())
    screen.fill((255, 255, 255))  # Fill the screen with white
    pygame.draw.rect(screen, ("yellow"), player)  # Draw the player rectangle
    pygame.draw.rect(screen, (255, 0, 0), apple)
    pygame.draw.rect(screen, (2,24,21), square)
    pygame.display.update()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS

    if player.colliderect(apple):
        score += 1
        print(score)
        apple.x = random.randint(0, 775)
        apple.y = random.randint(0, 575)

    if pygame.time.get_ticks() - start_time >= enemy_delay:

        if square.x <= player.x:
            square.x += 5
        if square.y <= player.y:
            square.y += 5
        if square.x >= player.x:
            square.x -= 5
        if square.y >= player.y:
            square.y -= 5

    if player.colliderect(square):
        print("YOU LOSE")
        running = False

    if score == 10:
        print("YOU WIN")
        running = False

pygame.quit()
sys.exit()