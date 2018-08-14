class Vector2():
	"""docstring for Vector2"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def translate(self, vector2):
		self.x += vector2.x
		self.y += vector2.y
		
class GameObject():
	"""docstring for GameObject"""
	def __init__(self, position = Vector2(0, 0)):
		self.position = position

	def setMesh(self, mesh):
		self.mesh = mesh