eighth = ("All around the World"[7].upper())

print(eighth)

kitchen = ("Pots", "Pans", "Knives")

print(kitchen[2])

# Activity 1: Create a program that stores someone’s name, age and favourite colour that prints this out in a complete sentence.

name = "Tsuki"
age = 4
favourite_colour = "Green"

print("Hello {}, nice to meet you! I see you are {} years old, what a grown up pup you are, when you go to the park you see your favourite colour {} everywhere.".format(name, age, favourite_colour))


# Activity 2: Create a program that stores what you eat today for breakfast, lunch and dinner, print these out. Update each of these variables to what you will eat tomorrow, print these out.

breakfast = "granola, yoghurt and berries"
lunch = "fajita wrap"
dinner = "pizza"

print("For breakfast today I ate {}, for lunch I had {} and for dinner I had {}.".format(breakfast, lunch, dinner))

breakfast = "ice cream" # updated food for tomorrow
lunch = "salad" # updated food for tomorrow
dinner = "pasta bake" # updated food for tomorrow

print("For breakfast tomorrow I will have {}, for lunch I will have {} and for dinner I will have {}.".format(breakfast, lunch, dinner))

# Activity 3: Create a program that calculates the number of days from today to your birth date and print this out.

from datetime import date
age = date.today()-date(1988,8,19)
print("I'm {} days old today!.".format(age.days))

# Activity 4: (1) Create a 9 variables space1, space2… space9
# (2) Assign either the value ‘x’, ‘o’, ‘ ‘ to each of these variable
# (3) Insert the variables into the board using format and make your board look like the one displayed

def game ():
    space1 = ""
    space2 = "x"
    space3 = "o"
    space4 = ""
    space5 = "o"
    space6 = ""
    space7 = "x"
    space8 = ""
    space9 = ""
    print("      |      |      |      ")
    print("    {}  |   {}  |   {}  |      ".format(space1,space2,space3))
    print("      |      |      |      ")
    print("---------------------------")
    print("      |      |      |      ")
    print("    {}  |   {}  |     {} |      ".format(space4,space5,space6))
    print("      |      |      |      ")
    print("---------------------------")
    print("      |      |      |      ")
    print("  {}   |  {}    |   {}   |      ".format(space7,space8,space9))
    print("      |      |      |      ")


game()



