import pygame

pygame.init()
W = 600
H = 400
x = W // 2
y = H // 2
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Task3")
red = (255, 0, 0)
white = (255, 255, 255)
speed = 10
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x = min(x + speed, W - 25)
            if event.key == pygame.K_LEFT:
                x = max(x - speed, 25) 
            if event.key == pygame.K_UP:
                y = max(y - speed, 25) 
            if event.key == pygame.K_DOWN:
                y = min(y + speed, H - 25)

    sc.fill(white)
    pygame.draw.circle(sc, red, (x, y), 25)
    pygame.display.update()
    clock.tick(60)