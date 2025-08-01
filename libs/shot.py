"""
Author: Andrés Torres
Date: 2025-08-01
Description: This module defines the Shot class, which represents a shot fired by the player.
"""

import pygame
from libs.circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt