class Team:
	def __init__(self, team_no, player_count):
		self.team_no = team_no
		self.player_count = player_count
		self.active = []

	def set_active(self, player):
		self.active.append(player)
		print(active + len(active))