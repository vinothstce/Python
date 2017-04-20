name = 'ML Programmer' #Name of the programmer
age = 31 # Age of the programmer
height = 74 # Height of the programmer
centimeters = height * 2.54 # height in centimeters
weight = 180 # Weight of the programmer
kilos = weight/2.2 # Weight in kilogram
eyes = 'Blue' # Eye color of the programmer
teeth = 'White' # Teeth color of the programmer
hair = 'Black' # Hair color of the programmer

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)) 


#Height in centimeter and Weight in Kilogram
print("He's %d centimeter in height" % centimeters)
print("He's %f kilogram in weight" % kilos)

