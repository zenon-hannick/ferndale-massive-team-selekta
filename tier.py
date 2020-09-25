from player import Player

class Tier:
	def __init__(self, tier_no, tier_score, player):
		self.tn = tier_no
		self.ts = tier_score
		self.players = []

	def add_player(self, player):
		if not isinstance(player, Player):
			raise Error("Invalid Player..")

		else self.players.append(player)

	def remove_player(self, player):
		if not isinstance(player, Player):
			raise Error("Invalid Player..")

		else self.players.remove(player)

	