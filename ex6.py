x = "There are %d types of people." % 10 # This line print the integer 10 in output
binary = "binary" # This line assign binary string to binary variable
do_not = "don't" # This line assign don't string to do_not variable
y = "Those who know %s and those who %s." % (binary, do_not) #This line print the binary and do_not variable

print x # This line print the variable x alone
print y# This line print the variable y alone

print "I said %r." % x # This line print the variable x along with string 
print "I also said: '%s'." % y# This line print the variable y along with string y

hilarious = False # This line assign a boolean value to a variable
joke_evaluation = "Isn't that joke so funny?! %r" #This variable is a combination of string with string format character

print joke_evaluation % hilarious #

w = "This is the left side of..." #Assigning a variable with string value on the same
e = "a string with a right side." #Assigning a variable with string value on the same

print w + e #printing a combination of two variable