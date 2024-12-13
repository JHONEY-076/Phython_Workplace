import random
import math

def sentence():
    print("This program is a 2-D guessing game")
    print("I will think of a point somewhere")
    print("between (1, 1) and (100, 100)")
    print("and give hints until you guess it.")
    print()

def get_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def hint_distance(distance):
    if distance <= 1.5:
        print("You're hot", end=" ")
    elif distance > 1.5 and distance <= 5.0:
        print("You're warm", end=" ")
    else:
        print("You're cold", end=" ")

def hint_direction(x1, y1, x2, y2):
    if x1 > x2 and y1 > y2:
        print("Go North East")
    elif x1 > x2 and y1 < y2:
        print("Go North West")
    elif x1 < x2 and y1 > y2:
        print("Go South East")
    elif x1 < x2 and y1 < y2:
        print("Go South West")

def game(x1, y1):
    count = 0  
    while True:
        input_value=input("Guess x and y:").split()
        x2 = int(input_value[0])
        y2 = int(input_value[1])
        
        count += 1
        distance = get_distance(x1, y1, x2, y2)
        hint_distance(distance)
        hint_direction(x1, y1, x2, y2)
        
        if x1 == x2 and y1 == y2:
            print(f"You got it right in {count} guesses!")
            break

def main():
    sentence()
    
    while True:
        x1 = random.randint(1, 20)
        y1 = random.randint(1, 20)
        
        game(x1, y1)
        
        question = input("Play again?")
        if question.lower() == "n":
            break
        
main()
