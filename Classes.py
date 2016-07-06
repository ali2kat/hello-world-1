import Base as Base

class Betterx(Base.Base):
	def __init__(self):
		self.x = 17

class BetterHam(Base.Base):
	def __init__(self):
		super(BetterHam, self).__init__()
	def betters(self):
		print ('Ham2')

class Combo(Betterx, BetterHam):
	def __init__(self):
		super(Combo, self).__init__()



if __name__ == '__main__':
	c=Combo()
	c.betters()
	print (c.x)
	print (Base.Base.__subclasses__())

		
