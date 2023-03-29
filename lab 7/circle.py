import pygame

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
red = (255, 0, 0)

screen.fill(white)

pygame.display.set_caption("Перемещение шара")

x = screen_width // 2
y = screen_height // 2

radius = 25

pygame.draw.circle(screen, red, (x, y), radius)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 20
            elif event.key == pygame.K_DOWN:
                y += 20
            elif event.key == pygame.K_LEFT:
                x -= 20
            elif event.key == pygame.K_RIGHT:
                x += 20
            
            if x - radius < 0:
                x = radius
            elif x + radius > screen_width:
                x = screen_width - radius
            if y - radius < 0:
                y = radius
            elif y + radius > screen_height:
                y = screen_height - radius
            
            screen.fill(white)
            
            pygame.draw.circle(screen, red, (x, y), radius)
            
            pygame.display.flip()

pygame.quit()
