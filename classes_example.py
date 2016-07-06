class Hero:
	'''
	What ever we want.
	'''
	def __init__(self,name):
		self.name=name
		self.health=100
	def eat(self,food):
		if (food =='apple'):
			self.health -=100
		elif (food == 'ham'):
			self.health += 20
bob=Hero("bob")
print bob.name
print bob.health
bob.eat("ham")
print bob.health