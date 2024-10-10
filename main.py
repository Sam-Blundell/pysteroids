import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updateable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
                print("Game Over")
                sys.exit()
            for shot in shots:
                if shot.check_for_collision(asteroid):
                    asteroid.split()
                    shot.kill()

        screen.fill((0, 0, 0))
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

