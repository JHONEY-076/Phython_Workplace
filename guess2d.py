import random
import math

MAX_COORDINATE = 20

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def give_direction_hint(x, y, target_x, target_y):
    direction = ""
    if target_y > y:
        direction += "north "
    elif target_y < y:
        direction += "south "
    
    if target_x > x:
        direction += "east"
    elif target_x < x:
        direction += "west"
    
    return direction.strip()

def give_hint(distance):
    if distance <= 1.5:
        return "hot!"
    elif distance <= 5.0:
        return "warm."
    else:
        return "cold."

def play_game():
    target_x = random.randint(1, MAX_COORDINATE)
    target_y = random.randint(1, MAX_COORDINATE)
    guesses = 0

    while True:
        x, y = map(int, input("Guess x and y: ").split())
        guesses += 1
        distance = calculate_distance(x, y, target_x, target_y)
        
        if distance == 0:
            print(f"You got it right in {guesses} guesses!")
            break
        
        hint = give_hint(distance)
        direction = give_direction_hint(x, y, target_x, target_y)
        print(f"You're {hint} Go {direction}")

    return guesses

def ask_to_play_again():
    response = input("Play again? ").lower()
    return response.startswith('y')

def display_statistics(total_games, total_guesses):
    if total_games > 0:
        print("\nOverall results:")
        print(f"Games played  = {total_games}")
        print(f"Total guesses = {total_guesses}")
        print(f"Guesses/game  = {total_guesses / total_games:.1f}")
    else:
        print("No games played.")

def main():
    total_games = 0
    total_guesses = 0

    print("This program is a 2-D guessing game.")
    print("I will think of a point somewhere")
    print("between (1, 1) and (100, 100)")
    print("and give hints until you guess it.")
    print()

    while True:
        total_games += 1
        guesses_in_game = play_game()
        total_guesses += guesses_in_game

        if not ask_to_play_again():
            display_statistics(total_games, total_guesses)
            break

if __name__ == "__main__":
    main()
