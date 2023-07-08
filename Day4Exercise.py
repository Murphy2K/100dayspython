rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
# Create a list of options for the game
options = [rock, paper, scissors]

# Ask the user to choose an option
valik = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Generate a random choice for the computer
comp = random.randint(0, 2)

# Print the user's and computer's choices
print(options[valik])
print(options[comp])

# Determine the winner of the game
if valik == comp:
    print("It's a draw!")
elif (valik - comp) % 3 == 1:
    print("You win!")
else:
    print("You lose!")