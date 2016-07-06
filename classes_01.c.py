class Base_Character(object):
	def printName(self):
		print(self.name)


##Non playable Charecters


class NonPlayable_Charecter(Base_Character):
	pass

class NPC_Friendly(NonPlayable_Charecter):
	pass

class NPC_Enemy(NonPlayable_Charecter):
##Self damage

	def __init__(self):
		self.attackDamage = 5

##---------------------------
# creating weapons

class Weapon (object):
	pass

##Playable Charecters


class Playable_Character(Base_Character):
	def __init__(self):
		self.weapon=Weapon()

class PC_Archer(Playable_Character):
	pass

class PC_GreenLantern(Playable_Character):
	pass

class PC_Butcher(Playable_Character):
	pass

if __name__ == '__main__':
	enemy = NPC_Enemy()
	print (enemy.attackDamage)
	butcher=PC_Butcher()
	print (butcher.weapon)




