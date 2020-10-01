from tier import Tier

class Player:
	def __init__(self, name, tier):
		self.name = name
		self.tier = tier
		self.playing = False
		self.phoneNumber = phoneNumber

		if not isinstance(tier, Tier):
			raise Error("Invalid Tier..")
		else self.tier = tier 

	def change_tier(self, tier):
		if not isinstance(tier, Tier):
			raise Error("Invalid Tier..")
		else:
			self.tier = tier

	def isPlaying(self):
		self.playing = True

	def addPhoneNumber(self, phoneNumber):
		self.phoneNumber = phoneNumber
	
	