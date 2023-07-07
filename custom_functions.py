def get_computer_player_count():
    while True:
        try:
            count = int(input("Izvēlies spēlētāju skaitu(1 - 9): "))
            if count >= 1 and count <= 9:
                return count
            else:
                print("Nepareiza ievade. Ievadiet ciparu no 1 līdz 9: ")
        except:
            print("Nepareiza ievade. Ievadiet ciparu no 1 līdz 9: ")


def get_round_count():
    while True:
        try:
            count = int(input("Izvēlies raundu skaitu(1 - 5): "))
            if count >= 1 and count <= 5:
                return count
            else:
                print("Nepareiza ievade. Ievadiet ciparu no 1 līdz 5:")
        except:
            print("Nepareiza ievade. Ievadiet ciparu no 1 līdz 5:")


def get_player_name():
    while True:
        name = input("Ievadiet spēlētāja segvārdu: ")
        if not name:
            print("Ievadiet spēlētāja segvārdu: ")
        else:
            return name


def get_user_option(options):
    option = None
    while (option not in options):
        option = input("Ievadiet savu izvēli (rock, paper, scissors, lizard, spock): ")
        if option.isdigit():
            option = int(option)
            if option >= 0 and option <= 4:   
                option = options[option]
                return option
    return option


# Game rules matrix to determ winer or loser
rules = {
    "rock": {"rock": "tie", "paper": "lose", "scissors": "win", "lizard": "win", "spock": "lose"},
    "paper": {"rock": "win", "paper": "tie", "scissors": "lose", "lizard": "lose", "spock": "win"},
    "scissors": {"rock": "lose", "paper": "win", "scissors": "tie", "lizard": "win", "spock": "lose"},
    "lizard": {"rock": "lose", "paper": "win", "scissors": "lose", "lizard": "tie", "spock": "win"},
    "spock": {"rock": "win", "paper": "lose", "scissors": "win", "lizard": "lose", "spock": "tie"}
}

# Read rules matrix
def win_or_lose(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    return rules[p1][p2]


# Increment winner points count
def update_points(player1, player2, results):
    if results == 'win':
        player1.points += 1
    elif results == 'lose':
        player2.points += 1    


# Make each palyer play against each other one time
def play_round(players, options):
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            # User against computer round
            if i == 0:
                players[i].roll = get_user_option(options)
                players[j].player_roll(options)
            # Computer against coumputer rounds
            else:
                players[i].player_roll(options)
                players[j].player_roll(options)
            # Get one game result
            result = win_or_lose(players[i].roll, players[j].roll)
            # Save game results
            update_points(players[i], players[j], result)
            # Print out one game result
            print("{0}! {1}({2}) : {4}({5}) (<<{3}>> PRET <<{6}>>)".format(
                result.upper(), 
                players[i].name, players[i].points, players[i].roll, 
                players[j].name, players[j].points, players[j].roll, 
                ))
            print("---------------------------------------------------------")
    return