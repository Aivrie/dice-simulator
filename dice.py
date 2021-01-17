''' 
Dice Simulator - A program imitates a rolling dice

Rules:
This script will generate a random number each dice the program runs, and the users can use the dice repeatedly
for as long as he wants. When the user rolls the dice, the program will generate a random number between
1 and 6 (as on a standard dice).

* The number will be displayed to the user.
* It will also ask user(s) if they would like to roll the dice again.
* The program should also include a function that can randomly grab a number within 1 to 6 and print it.
'''

import random

# Step 1: Create a dice class with a roll function
class Dice:
    # Step 2: Define the roll function - Function should randomly select a function between 1-6
    def roll(self):
        roll = []
        # Roll function to select a number between 1-6
        for elem in range(1, 7):
            roll.append(elem)
            # print(roll)
        computer = random.choice(roll)
        
        # Step 3: Display number to the user
        return computer        


# Game Loop
while True:
    d = Dice()
    print(d.roll())
    another_roll = input('Want to roll dice again? Type "yes" to roll dice: ')
    if another_roll.lower() == 'yes':
        continue
    else:
        break


    


# Step 4: Ask user of he/she would like to roll again
