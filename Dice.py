import random


def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll


while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4.")
    else:
            print("Invalid number, try again.")

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores)< max_score:

    for player_index in range(players):
        print("\nPlayer", player_index + 1, "turn has just started!")
        print("Your total score is:", players_scores[player_index], "\n")
        current = 0

        while True:
            should_roll = input("would you like to roll (y)?")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current = 0
                break
            else:
                current += value
                print("You rolled a:", value)

            print("Your score is: ", current)

        players_scores[player_index] += current
        print("Your total score is:", players_scores[player_index])

max_score = max(players_scores)
winning = players_scores.index(max_score)
print("Player number", winning + 1, "is the winner with the score of: ", max_score)