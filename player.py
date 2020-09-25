class Player:
	def __init__(self, name, tier):
		self.name = name
		self.tier = tier

		if not isinstance(tier, Tier):
			raise Error("Invalid Tier..")
		else self.tier = tier 

	def add_tier(self, tier):
		if not isinstance(tier, Tier):
			raise Error("Invalid Tier..")
		else:
			self.tier = tier
	