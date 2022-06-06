import pygame as pg

BALLSPEED = 10

class Platform(pg.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.image = pg.Surface((60, 10))
		self.rect = self.image.get_rect(center=(400, 590))
		self.image.fill((255, 0, 0))

	def update(self, keys, *args, **kwargs):
		step = 15
		if keys[pg.K_a] and self.rect.left >= step:
			self.rect.x -= step
		if keys[pg.K_d] and self.rect.right <= 800 - step:
			self.rect.x += step

class Ball(pg.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.image = pg.Surface((16, 16), pg.SRCALPHA, 32)
		pg.draw.circle(self.image, (255, 255, 255), (8, 8), 8)
		self.rect = self.image.get_rect(center=(400, 500))
		self.speed_x = BALLSPEED
		self.speed_y = -BALLSPEED
		self.score = 0
		self.isMoving = True

	def update(self, platform, *args, **kwargs):
		if not self.isMoving:
			return

		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

		if self.rect.right > 800:
			self.speed_x = -self.speed_x
			self.rect.right = 800

		if self.rect.left < 0:
			self.speed_x = -self.speed_x
			self.rect.left = 0

		if self.rect.top < 0:
			self.speed_y = -self.speed_y
			self.rect.top = 0
