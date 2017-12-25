"""Paper Rock Scissors"""

from random import randint
from time import sleep

options = ['R', 'P', 'S']

LOSS_MESSAGE = "You lost!"
WINNING_MESSAGE = "You win!"

def decide_winner(user_choice,computer_choice):
  print "You have selected %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "Computer has selected %s" % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "It is a TIE!!"
  elif user_choice_index == 0 and computer_choice_index == 2:
  	print WINNING_MESSAGE
  elif user_choice_index == 1 and computer_choice_index == 0:
  	print WINNING_MESSAGE
  elif user_choice_index == 2 and computer_choice_index == 1:
  	print WINNING_MESSAGE
  elif user_choice_index > 2:
  	print "Invalid option"
    
  else:
  	print LOSS_MESSAGE
  
def play_RPS():
  print "Paper, Rock or Scissors"
  
  user_choice = raw_input("Select R for Rock, P for Paper or S for Scissors: ")
  user_choice = user_choice.upper()
  sleep(1)
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice,computer_choice)
  
play_RPS()