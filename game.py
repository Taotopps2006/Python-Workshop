import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

background = pygame.Surface(screen.get_size())

running = True
x = 100
y = 100

ball_surface = pygame.Surface((200, 200))
pygame.draw.circle(ball_surface, (0, 255, 255), (x, y), 25)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 5
            if event.key == pygame.K_RIGHT:
                x += 5
            if event.key == pygame.K_UP:
                y -= 5
            if event.key == pygame.K_DOWN:
                y += 5
        screen.blit(background, (0,0))
        screen.blit(ball_surface, (round(x), round(y)))
    pygame.display.flip()

pygame.quit()