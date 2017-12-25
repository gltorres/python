"""Mad Libs"""
print "Mad Libs has started..."

name = raw_input("Enter the name of your character...")

adj1 = raw_input("Enter one adjetive: ")
adj2 = raw_input("Enter another one: ")
adj3 = raw_input("Enter just one more: ")

verb1 = raw_input("Now we need verbs, give me the first one: ")
verb2 = raw_input("A second one: ")
verb3 = raw_input("And a last one: ")

noun1 = raw_input("Lets get some nouns, give me one: ")
noun2 = raw_input("Give me a second one: ")
noun3 = raw_input("One more: ")
noun4 = raw_input("The last one! ")

animal = raw_input("Give me an animal: ")
food = raw_input("What food do you like?: ")
fruit = raw_input("What about fruit? Pick one: ")
number = raw_input("Give me an number: ")
superhero = raw_input("Who is your superhero?")
country = raw_input("Now I need a country: ")
dessert = raw_input("And a dessert: ")
year = raw_input("And at last, one year: ")




#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print STORY % (adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, number, name, superhero, superhero, name, country, name, dessert, name, year, noun4)