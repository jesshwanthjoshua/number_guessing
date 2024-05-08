from art import logo
from replit import clear
import random

guessing_game = True

def difficulty(level):  
  if level == "easy":
    lives = 10
  elif level == "hard":
    lives = 5
    
  print(f"You have total lives of {lives}")
  return lives
  
def calculate(guess, lives, number):
    
  if guess == number:
    print("\nYou have guess it correct. You Win.\n")
    lives = 0
  
  else:
    lives -= 1
    print(f"\nYou lost a life. Remainging lives= {lives}\n")
  
    if (guess - number) < -25:
      print("Your guess is too much far.")
  
    elif (guess - number) >= -25 and (guess-number) < -10:
      print("Your guess is not so far from actual number.")
  
    elif (guess - number) >= -10 and (guess - number) < 0:
      print("Your guess is near the actual number.")
  
    elif (guess - number) > 0 and (guess - number) <= 10:
      print("Your guess is near the actual number.")
  
    elif (guess-number) > 10 and (guess - number) <= 25:
      print("Your guess is not far from actual number.")
  
    elif (guess - number) > 25:
      print("Your guess is too much far.")
  
    if lives == 0:
      print(f"You lost all lives. You Lose. The actual number is {number}.")

  return lives

def game():
  print(logo)
  number = random.randint(1,100)
  # print(f"The number is: {number}")
  
  level = input ("Choose your difficulty level 'easy' or 'hard':  ").lower()
  lives = difficulty(level)
  
  while lives > 0:
    guess = int(input("Type your guess: "))
    
    lives = calculate(guess, lives, number)


while guessing_game is True:
  game()
  
  if input("\nType 'y' if you want to start with a new game, or 'n' to stop the game: ").lower()  == 'y':
    clear()
    
  else:
    guessing_game = False
