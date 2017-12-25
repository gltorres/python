"""Command Line Calendar"""
from datetime import datetime
from time import sleep, strftime

USER_NAME = "Alex"

calendar = {}

def welcome():
  print "Welcome ", USER_NAME, " I hope you are doing alright!"
  print "Your calendar will be ready in a second"
  sleep(1)
  print strftime("%A %m %d, %Y")
  print strftime("%H:%M")
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while(start):
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Your Calendar is empty..."
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Adding..."
      sleep(1)
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY)")
      if len(date)>10 or int(date[6:]) < int(strftime("%Y")):
        print "Wrong format date..."
        try_again = raw_input("Try again? Y for yes, N for no")
        try_again = try_again.upper()
        if try_again == "Y":
          start = True
        else:
        	start = False
      else:
        calendar[date] = event
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
         print "The clanedar is empty..."
      else:
        event = raw_input("What event? ")
        for key in calendar.keys():
          if calendar[key] == event:
            del calendar[key]
            print "Deletion complete"
            print calendar
            break
        else:
           print "That event does not exist..."
    elif user_choice == "X":
      start = False
    else:
      print "Garbage!!!!"
                                
start_calendar()