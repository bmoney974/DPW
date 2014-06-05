
# User Inputs ===========================

name = raw_input("Enter your name ")
state = raw_input("Enter your birth state ")
color = raw_input("Enter your favorite color ")
age = raw_input("Enter your age ")
siblings = raw_input("Enter you number of siblings ")
dollars = raw_input("Enter a number between 1 and 1000 ")
# ==============================================





# Mad Lib Story ==============================================
story = "Hi my name is  " + name + " and I was born in the state of " + state + ". My favorite color is " + color +" . I am " + str(age) + " years old and I have " + str(siblings) + " siblings and I will give you "+ str(dollars) + " dollars. Sike Im just playing"


print story
# ==============================================



# array ============================
planets = ["Earth", "Mars", "Venus"]


print "Here is a fun fact, I bet your were born on one of these planets. "
for p in planets:
    print p
# ==============================================





# Math ==============================================

print "Hey did you know I can do math would you like to see?"

lets_do_math = raw_input("Enter Y or N ")

a = 5 + 1
b = 6 - 4
c = 10 / 2

# ==============================================




# Conditional Satment ==============================================

yes = "y"
yes2 = "Y"
no = "n"
no2 = "N"
math = "5 + 1 = " + str(a) + " and 6 - 4 = " + str(b) + " and 10 / 2 = " + str(c)

if lets_do_math == yes or lets_do_math == yes2:
    print math + " Pretty good hunh!"
elif lets_do_math != yes or lets_do_math != yes2:
    print " Awe man im pretty good that sucks."
else:
    print "Please make a choice"

if int(age) > 20:
    print " Hey " + name + " it seems you are " + age + " years old lets get a beer!"
else:
    print "Sorry " + name + " your only " + age + " years old so you not old enough to drink yet, Bummer"
# ==============================================



#  Function ==============================================
def calcYear(current_year, age):
    birth_year = current_year - int(age)
    return birth_year
d = calcYear(2014, int(age));
print "According to your age it's a 95% chance your were born in " + str(d)

def calcArea(l, w):
    area = l * w
    return area

e = calcArea(100, 70);


print " Just a random thought. A rectangle with a length of 100 feet and a width of 70 feet has an area of " + str(e) + " Square Feet"
# ==============================================



# Dictionary ==============================================
Tv_shows = dict()
Tv_shows = {"Walking Dead":"Zombie", "Battlestar Galactica":"Cyborg", "Falling Skies":"Alien"}

print "I think this Halloween I'm going to dress up like a " + Tv_shows["Walking Dead"]

# ==============================================



# assignment operators==============================================

f = 17
g = 91

f += g
g -= f
# ==============================================
