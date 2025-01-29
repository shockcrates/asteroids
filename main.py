import pygame
from constants import *
import player
import asteroid
import asteroidField
import sys
import shot

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock1 = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	player.Player.containers = (updatable, drawable)
	asteroid.Asteroid.containers = (asteroids, updatable, drawable)
	asteroidField.AsteroidField.containers = (updatable)
	shot.Shot.containers = (shots, drawable, updatable)
	bob = player.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	the_field = asteroidField.AsteroidField()

	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill("black")
		for object in updatable:
			object.update(dt)
		
		for aster in asteroids:
			if aster.collision_detection(bob):
				print("Game Over!")
				sys.exit()
			for shotty in shots:
				if aster.collision_detection(shotty):
					shotty.kill()
					aster.split()

		for object in drawable:
			object.draw(screen)
		pygame.display.flip()
		dt = clock1.tick(60) / 1000

if __name__ == "__main__":
	main()
