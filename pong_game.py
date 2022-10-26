import pygame
pygame.init()


SIZE = width, height = (800, 800)
WHITH = 255, 255, 255
BLACK = 0,0,0
SCREEN = pygame.display.set_mode(SIZE)
WIN = pygame.display.set_caption("pong game made by @aditya1366")
SCREEN.fill(BLACK)
pygame.display.update()


FPS = 60
run = True
clock = pygame.time.Clock()





while run:
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

if __name__ == '__main__':
    main()


