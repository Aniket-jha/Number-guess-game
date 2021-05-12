
from art import logo
import random
from replit import clear
EASY_LEVEL=10
HARD_LEVEL=5


def comparison(guess,random_input,turns) :
  """checks answers against guess and return the number of turns"""
  if guess > random_input :
    print("Your guess is too high. Try again.")
    return turns-1
   
  elif guess < random_input :
    print("Your guess is too low. Try again.")
    return turns-1
  else : 
    print(f"You guessed it right.The correct answer is {random_input}")
    


def set_difficulty() :
  level_you_want= input("Choose a difficulty. Type 'easy' or 'hard': \n ")
  if level_you_want == "easy" :
   return  EASY_LEVEL
  else :
    return HARD_LEVEL



def game() :
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  random_input = random.randint(1,100)
  print(f"Your random anwers {random_input} ")
  turns = set_difficulty()
  guess=0
  while guess != random_input :
    print(f"You have {turns} attempts remaining to guess the answers.")
    guess=int(input("Make a guess :"))
    turns = comparison(guess, random_input, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != random_input:
      print("Guess again.")


game()
play_again=input("do you want to play again 'y' if want to and 'n' if you don't: \n ")
if play_again=="y" :
  clear()
  game()
