class BaseClass(object):
	def printHam(self):
		print 'ham'

class InhartingClass(BaseClass):
	pass

x = InhartingClass()
x.printHam()
		