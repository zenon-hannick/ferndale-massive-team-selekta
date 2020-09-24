# TNF Team Picker

class Tier:
	def __init__(self, tier_no, tier_score):
		self.tn = tier_no
		self.ts = tier_score
		self.players = []

class Player:
	def __init__(self, name, Tier):
		self.name = name
		self.Tier = Tier

class Team:
	def __init__(self, team_no, player_count):
		self.team_no = team_no
		self.player_count = player_count
		self.active = []

	def set_active(self, player):
		self.active.append(player)
		print(active + len(active))

T1 = Tier(1, 8)
T6 = Tier(6, 3)
p1 = Player("Joel", 6)
p2 = Player("Adam", 1)




