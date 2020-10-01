from player import Player
from team import Team

class PlayerPool:
	def __init__(activePlayers):
		activePlayers = []

	def setActive(player):
		if not isinstance(player, Player):
			raise Error("Invalid Player..")
		elif self.playing.player is True:
			activePlayers.append(player)
		else:
			pass

	def clearActive():
		self.activePlayers.clear()

	def removePlayer(player):
		if not isinstance(player, Player):
			raise Error("Invalid Player..")
		elif player is not in activePlayers:
			raise Error(f"{self.player} was not in the active player list")
		else:
			activePlayers.remove(player)

	