# Asteroids Game
# Author: Andrés Torres
# Date: 2025-08-01
# This is the main file for run the game

import pygame
from constants import *
from libs.player import Player
from libs.asteroid import Asteroid
from libs.asteroidfield import AsteroidField
from libs.shot import Shot

def main():
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
        
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        dt = clock.tick(60)/1000
        
        for item in drawable:
            item.draw(screen)
            
        updatable.update(dt)
        
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision_detection(asteroid):
                    bullet.kill()
                    asteroid.split()
            if asteroid.collision_detection(player):
                print("Game over!")
                return
                
        pygame.display.flip()

if __name__ == "__main__":
    main()