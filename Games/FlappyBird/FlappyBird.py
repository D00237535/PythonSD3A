import pygame, sys, time
from FlappyBirdSettings import *
from sprites import BG


class Game:
    def __init__(self):

        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        BG(self.all_sprites)

        def run(self):
            last_time = time.time()
            while True:

                dt = time.time() - last_time
                last_time = time.time()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


if __name__ == '__main__':
	game = Game()
	game.run()