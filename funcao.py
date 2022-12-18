class calc:
	def __init__(self, a, b):
		self.a = a 
		self.b = b
		
	def soma(self):
		c = self.a + self.b
		return print(c)
	
	def sub(self):
		c = self.a - self.b
		return print(c)
	
	def mult(self):
		c = self.a * self.b
		return print(c)
 	
	def div(self):
		c = self.a / self.b
		return print(c)


if __name__ == '__main__':
		num = calc(5,2)
		num.div()
		