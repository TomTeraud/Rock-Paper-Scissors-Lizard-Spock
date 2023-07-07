from custom_functions import get_computer_player_count, get_round_count, play_round, get_player_name
from custom_classes import Player

options = ('rock', 'paper', 'scissors', 'lizard', 'spock')
computer_names = (
    'Citplanētietis', 
    'Pirāts', 
    'Spiegs', 
    'Kokgrauzis', 
    'Grāmatutārps', 
    'Dziedātājs', 
    'Pelnrušķis', 
    'Zeltakāja', 
    'Ķirurgs',
)


# Get user input
computer_count = get_computer_player_count()
round_count = get_round_count()
player_name = get_player_name()

# Create empty list where store player objects.
players = []

# Create player object and append to players list
player = Player(player_name)
players.append(player)

# Generate list of computer players using Computer class and append to players list
for i in range(computer_count):
    player = Player(computer_names[i])
    players.append(player)

# Play all rounds for all players and save their score
for i in range(round_count):
    print()
    print("ROUND: {}!".format(i + 1))
    play_round(players, options)

# Sort players based on points in descending order
sorted_players = sorted(players, key=lambda x: x.points, reverse=True)

# Print out points in order
print()
print("Spēles beigas!")
print("Spēlētāji ieguva šādu uzvaru skaitu:")
for player in sorted_players:
    print("{}: {}".format(player.name, player.points))
# Get overal vinner
if sorted_players[0].points != sorted_players[1].points:
    print()
    print("Spēli uzvarēja {}!!!". format(sorted_players[0].name))
else:
    print()
    print("Spēlei nav uzvarētāja! Neviens spēlētājs nav ieguvis lielāku uzvaru skaitu par pārējo spēlētāju uzvarām")