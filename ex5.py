my_name = 'ML Programmer' #Name of the programmer
my_age = 31 # Age of the programmer
my_height = 74 # Height of the programmer
my_weight = 180 # Weight of the programmer
my_eyes = 'Blue' # Eye color of the programmer
my_teeth = 'White' # Teeth color of the programmer
my_hair = 'Black' # Hair color of the programmer

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)) 