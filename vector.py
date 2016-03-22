class Vector:
	def __init__(self, n, coord):
		self.n = n
		self.coord = coord
	def __add__(self, b):
		if (self.n == b.n):
			c = Vector(self.n, [])
			for i in range(0,b.n):
				c.coord.append(self.coord[i] + b.coord[i])
			return(c)
		else: print('Not defined')
	def __sub__(self, b):
		if (self.n == b.n):
			c = Vector(self.n, [])
			for i in range(0,b.n):
				c.coord.append(self.coord[i] - b.coord[i])
			return(c)
		else: print ('Not defined')
	def __mul__(self, b):
		if (self.n == b.n):
			c = Vector(self.n, [])
			for i in range(0,b.n):
				c.coord.append(self.coord[i]*b.coord[i])
			return(c)
		else: print('Not defined')
a = Vector(3, [1,2,7])
b = Vector(3,[3,4,0])
c = a + b
d = a - b
e = a * b
print(c.n, c.coord, d.n, d.coord, e.n, e.coord)
