class Ham:
	def __init__(self):
		self.name = 'ham'
		self.healthBounus = 10
class Hero:
	def __init__(self):
		self.health = 100
	def eat (self,food):
		self.health += food.healthBounus
bob = Hero()
ham = Ham()
bob.eat(ham)
print (bob.health)
