import pygame
import circleshape
from constants import *
import shot
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS < self.radius:
            random_angle = random.uniform(20, 50)
            pos_new_vector = self.velocity.rotate(random_angle)
            neg_new_vector = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first_child = Asteroid(self.position.x, self.position.y, new_radius)
            first_child.velocity = pos_new_vector * 1.2

            second_child = Asteroid(self.position.x, self.position.y, new_radius)
            second_child.velocity = neg_new_vector * 1.2