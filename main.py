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
    pygame.display.set_caption("Asteroids Game")
    font = pygame.font.SysFont(None, 36)
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    score = 0
    lives = 3
    respawn_timer = 0
    respawn_delay = 2.0

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        if respawn_timer > 0:
            respawn_timer -= dt
        else:
            if not player.alive():
                if lives > 0:
                    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                else:
                    print("Game over!")
                    return

        updatable.update(dt)

        if player.alive() and respawn_timer <= 0:
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    lives -= 1
                    player.kill()
                    respawn_timer = respawn_delay
                    break
                
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score += 5

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
            
        # Display score and lives
        score_text = font.render(f"Score: {score}", True, pygame.Color("white"))
        lives_text = font.render(f"Lives: {lives}", True, pygame.Color("white"))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    