"""
Author: Andrés Torres
Date: 2025-08-01
Description: This module defines the CircleShape class, which serves as a base for the other game objects, all objects are circles for simplicity.
"""

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision_detection(self, circle):
        distance = self.position.distance_to(circle.position)
        return distance <= self.radius + circle.radius