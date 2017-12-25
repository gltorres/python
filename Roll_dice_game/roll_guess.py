"""Roll a dice!"""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Guess a number: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The max value is ", str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val or user_guess < 2:
    print "The number is too large or smaller than 2..."
    return 0
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is %d" % first_roll
    sleep(1)
    print "The second roll is %d" % second_roll
    total_roll = first_roll + second_roll
    print "The total roll is %d" % total_roll
    
    print "Result... ",
    sleep(1)
    if user_guess > total_roll:
      print "YOU WON!! CONGRATULATIONS!"
      return 0
    else:
      print "Oops, you lost, try again!"
      return 0

roll_dice(6)
    