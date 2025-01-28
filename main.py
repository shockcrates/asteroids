import pygame
from constants import *
import player

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock1 = pygame.time.Clock()
	dt = 0

	bob = player.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill("black")
		bob.draw(screen)
		pygame.display.flip()
		dt = clock1.tick(60) / 1000

if __name__ == "__main__":
	main()
