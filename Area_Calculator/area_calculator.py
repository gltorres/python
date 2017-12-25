"""Area Calculator"""
from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "Calculator is starting up..."
sleep(1)
print "Current time: %s/%s/%s %s:%s" % (now.month,now.day,now.year, now.hour, now.minute)
hint = "Don't forget to include the correct units!\nExiting..."

option = raw_input("Enter C for Circle or T for Triangle: ")

option = option.upper()

if option == 'C':
  radius = float(raw_input("Enter the radius: "))
  area = (radius ** 2) * pi
  print "The Pie is baking..."
  sleep(1)
  print "The area is: %.2f" % area
elif option == 'T':
  base = float(raw_input("Enter the base: "))
  height = float(raw_input("Enter the height: "))
  area = (base * height) / 2.0
  print "Uni Bi Tri..."
  sleep(1)
  print "The area is: %.2f" % area
else:
  print "Garbage..."
  