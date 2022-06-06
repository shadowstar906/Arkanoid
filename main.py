import pygame as pg
from game_objects import Platform, Ball

class Game:
	def __init__(self):
		self.score = 0
		self.game_over = False
		self.sprites = pg.sprite.Group()
		self.platform = Platform()
		self.sprites.add(self.platform)
		self.ball = Ball()
		self.sprites.add(self.ball)

	def process_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				return True
			elif event.type == pg.MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()

	def run_logic(self):
		pass

	def display_frame(self, screen, keys):
		screen.fill((0, 0, 0))
		self.sprites.update(keys=keys, platform=self.platform)
		self.sprites.draw(screen)
def main():
	pg.init()

	pg.display.set_caption('Arkanoid')
	screen = pg.display.set_mode((800, 600))
	clock = pg.time.Clock()

	game = Game()
	endgame = False

	while not endgame:
		endgame = game.process_events()
		game.run_logic()
		keys = pg.key.get_pressed()
		game.display_frame(screen, keys)

		pg.display.update()

		clock.tick(30)

if __name__ == '__main__':
	main()