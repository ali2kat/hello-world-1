class AddFive:
	def add(self,var):
		return var + 5
class Num:
	def __init__(self, value):
		self.val = value
		self.otherVal = None
n = Num(15)
a5 = AddFive()
n.otherVal = a5.add(n.val)
print (n.val, n.otherVal)