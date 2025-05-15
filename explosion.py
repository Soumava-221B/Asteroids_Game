import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, max_radius=40, duration=0.5):
        super().__init__(self.containers)
        self.position = pygame.Vector2(position)
        self.max_radius = max_radius
        self.duration = duration
        self.elapsed = 0

    def update(self, dt):
        self.elapsed += dt
        if self.elapsed > self.duration:
            self.kill()

    def draw(self, screen):
        progress = self.elapsed / self.duration
        radius = int(self.max_radius * progress)
        alpha = max(0, 255 * (1 - progress))

        surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, (255, 100, 0, int(alpha)), (radius, radius), radius)
        screen.blit(surface, (self.position.x - radius, self.position.y - radius))