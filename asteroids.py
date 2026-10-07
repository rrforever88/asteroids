from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)


    def update(self, dt) -> None:
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand = random.uniform(20.0, 50.0)
            ast_one_move = self.velocity.rotate(rand)
            ast_two_move = self.velocity.rotate(-rand)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            ast_one = Asteroid(self.position.x, self.position.y, new_radius)
            ast_two = Asteroid(self.position.x, self.position.y, new_radius)

            ast_one.velocity = ast_one_move * 1.2
            ast_two.velocity = ast_two_move * 1.2

        
