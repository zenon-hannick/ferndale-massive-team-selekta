from team import Team 
from player import Player
from tier import Tier
from playerPool import PlayerPool
import csv

# # Manual process currently used:
# # - Add active players to the spreadsheet
Team1 = Team(1)
Team2 = Team(2)

Tier1 = Tier(1, 6)
Tier2 = Tier(2, 5)
Tier3 = Tier(3, 4)
Tier4 = Tier(4, 3)
Tier5 = Tier(5, 2)
Tier6 = Tier(6, 1)

# Import players using csv file. Use csv dictionaries to create Player objects.
# Could do the same for Tier as it would allow me to change them in bulk easier. 
with open('TNFDB.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	next(csv_reader)

	for line in csv_reader:
		print(line)
# - blackout all players who arent playing

# - create number of teams required

# - add players in to each side to create equal valued teams

# - ensure equal spread of different style players