from graphics import *

class BricksWall():
	"""docstring for BricksWall"""
	def __init__(self,tam = 20, itam = 5, esp = 2, off = color_rgb(124, 124, 124), on = color_rgb(64, 64, 64)):
		self.i = 20
		self.j = 10
		self.esp = esp
		self.tam = tam
		self.itam = itam
		self.off = off
		self.on = on
		width = self.j * (self.tam + self.esp) + 200
		height = self.i * (self.tam + self.esp) + 6
		self.win = GraphWin('Briks', width, height, autoflush=False)
		self.contruction()

	def contruction(self):
		self.wall = []
		for i in range(0, self.i):
			line = []
			for j in range(0, self.j):
				rec = Rectangle(Point(0, 0), Point(self.tam, self.tam))
				irec = Rectangle(Point(self.itam, self.itam), Point(self.tam - self.itam, self.tam - self.itam))
				rec.setOutline(self.off)
				irec.setFill(self.off)
				irec.setOutline(self.off)
				dx = (j * self.tam) + (j * self.esp) + self.esp
				dy = (i * self.tam) + (i * self.esp) + self.esp
				rec.move(dx, dy)
				irec.move(dx, dy)
				rec.draw(self.win)
				irec.draw(self.win)
				line.append([rec, irec])
			self.wall.append(line)
		b = Rectangle(Point(-5, -5), Point(rec.getP2().x + 5, rec.getP2().y + 5))
		b.setWidth(2)
		b.draw(self.win)

	def clean(self):
		for i in range(0, self.i):
			for j in range(0, self.j):
				self.wall[j][i][0].setOutline(self.off)
				self.wall[j][i][1].setFill(self.off)
				self.wall[j][i][1].setOutline(self.off)