from player import Player
from playerPool import PlayerPool

class Team:
	def __init__(self, team_no):
		self.team_no = team_no
		self.player_count = player_count
		self.lineup = []
		self.scoreList = []
		self.teamScore = teamScore

	def clearLineup(self):
		self.lineup.clear()

	def addTeamScore(self):
		for n in range(self.lineup):
			self.scoreList.append(tier_score)
		teamScore = sum(self.scoreList)
		print ("Team Score is:", teamScore)
