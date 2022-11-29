import pygame as pg 
from pygame.constants import *

class NotProButCreate(object):
	def __init__(self, width, height):
		self.window = pg.display.set_mode((width,height))
		self.canvas = pg.Surface((width,height))
		self.canvas.fill((255,255,255))
		self.runnning = True
		self.last_mpos = None
		self.click = False
		self.line_width = 1
		self.line_widthx = self.line_width
		self.line_widthy = self.line_width
		self.line_color = [0, 0, 0]
		pg.display.set_caption("Не Procreate, но тоже сойдет")

	def events(self):
		for e in pg.event.get():
			if e.type == QUIT:
				self.runnning = False
				break

			if e.type == MOUSEBUTTONDOWN:
				self.click = True
				# print('Works')

			if e.type == MOUSEBUTTONUP:
				self.click = False
				self.last_mpos = None

	def update(self):
		mx, my = pg.mouse.get_pos()

		if not self.last_mpos is None and self.click:
			mx0, my0 = self.last_mpos

			for x in range(self.line_widthx):
				for y in range(self.line_widthy):

					pg.draw.line(self.canvas, 
						self.line_color, 
						(mx0 + x + self.line_widthx/2, my0 + y + self.line_widthy/2), 
						(mx + x + self.line_widthx/2, my + y + self.line_widthy/2))

		self.last_mpos = (mx, my)

	def render(self):
		self.window.blit(self.canvas, (0,0))

	def mainloop(self):
		self.runnning = True
		while self.runnning:
			self.events()
			self.update()
			self.render()
			pg.display.flip()

def main():
	mainclass = NotProButCreate(640, 480)
	mainclass.mainloop()

if __name__ == "__main__":
	main()
