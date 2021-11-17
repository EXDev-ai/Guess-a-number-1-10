import random

BAD_ATTEMPT_MESSAGE = "Oops, that wasn't the right answer! Try again. \n"
GUESS_MESSAGE = "Enter a number between 1 and 10 to guess. Type hint for a hint."

number_chosen = 1  

def choose_number():
  global number_chosen 
  number_chosen = random.randint(1,10)
choose_number()

def game():
  attempts = 5
  player_input = input(GUESS_MESSAGE)
  if player_input.isnumeric():
    player_input = int(player_input)
  if player_input == "hint":
    if number_chosen <= 5:
      print("The number to guess is below or equal to 5.")
    elif number_chosen >= 6:
      print("The number to guess is above or equal to 6.")
  if player_input != number_chosen and player_input != "hint":
   print(BAD_ATTEMPT_MESSAGE)
   if attempts > 0:
     attempts = attempts - 1
   elif attempts <= 0:
    print(f"Looks like you're out of tries. The number was {number_chosen}. Better luck next time!")
  if player_input == number_chosen:
    print(f"You got it! The number is {number_chosen}.")
    game()
    
while True:
 game()