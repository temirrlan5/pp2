import pygame

pygame.init()
W = 600
H = 400
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

music_list = ["Lab7/Sakura-Girl-Motivation-chosic.com_.mp3", "Lab7/simple-piano-melody-9834.mp3"]
index = 0
track = pygame.mixer.Sound(music_list[index])

playing = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    track.stop()
                    playing = False
                else:
                    track.play()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                track.stop()
                index += 1
                track = pygame.mixer.Sound(music_list[index])
                if playing:
                    track.play()
            elif event.key == pygame.K_LEFT:
                track.stop()
                index -= 1
                track = pygame.mixer.Sound(music_list[index])
                if playing:
                    track.play()

    pygame.display.update()
    clock.tick(60)