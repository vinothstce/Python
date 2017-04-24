import sys
s = "Hello"
s2 = s.upper()
s3 = s.lower()
s4 = s.count('o')
print s2
print s3
print s4
#Strings are immutable, so no string method can change the original string, it can only return a new string. Confirm this by entering each line individually in the Shell to see the original s is unchanged:
print s

#Python lets you see all the methods that are bound to an object (and any object of its type) with the built-in function dir. To see all string methods, supply the dir function with any string. For example, try in the Shell:
print dir(sys)

print dir(str)
help(str.strip)

#Unlike Java, the '+' does not automatically convert numbers or other types to string form. The str() function converts values to a string form so they can be combined with other strings.
pi = 3.14
#text = 'The value of pi is ' + pi
text = 'The value of pi is' + str(pi)
print text

a = ['a', 'bb', 'ccc']

#For numbers, the standard operators, +, /, * work in the usual way.
# There is no ++ operator, but +=, -=, etc. work. 

#Built in String Methods
s = " It was the best of times. It was the worst of times.    "
q = 'T'.join(a)
print q
print s.lower() # returns the lowercase or uppercase version of the string
print s.upper() # returns the lowercase or uppercase version of the string
print s.strip() #returns a string with whitespace removed from the start and end
print s.lstrip()# remove leading space or left strip 
print s.rstrip()# remove trailing space or right strip
print s.startswith('') #tests if the string starts or ends with the given other string
print s.endswith('.') # tests if the string starts or ends with the given other string
print s.find('was') # searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
print s.replace('the', 'hello')
print s.index('was') # both find and index do the same thing
print s.count('was')# count the number of occurance of a thing
print ' '.join(reversed(s))
print "Hello" + " " + "World"
print q.split('T') #s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.

#Testing string methods
print "hi+".isalnum() #check if all char are alphanumeric
print "Hello".isalpha() #check if all char in the string are alphabetic
print "123".isdigit() #test if string contains digits
print "This Contain Title".istitle() #test if string contains title words i.e First character of a string in capital
# islower, isupper, and istitle return True if the string is in lowercase, uppercase, or titlecase respectively. Uncased characters are "allowed", such as digits, but there must be at least one cased character in the string object in order to return True.
#str.istitle()
#Return true if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return false otherwise.
print "HELLO".isupper()
print "hello".islower()
s = "h     "
print s

 
 #The slice s[start:end] is the elements beginning at start and extending up to but not including end. Suppose we have s = "Hello"
 # H  e  l  l  o
 # 0  1  2  3  4
 #-5 -4 -3 -2 -1
 
s = "Hello"
print s[1:4] # chars starting at index 1 and extending up to but not including index 4
print s[1:] # omitting either index defaults to the start or end of the string
print s[:] #'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
print s[:100] # is 'ello' -- an index that is too big is truncated down to the string length
# Neglecting character from the beginning
print s[1:] 
print s[2:]
print s[3:]
print s[4:]
print s[5:]
#Neglecting character from end
print s[:-1]
print s[:-2]
print s[:-3]
print s[:-4]
print s[:-5]
e = 'you'
p = 'plan'
i = 54
print "Hello how are %s , what is your future %s, i am %d,  how old are you" %(e, p, i)
speed = 100
mood = 'terrible'
if speed >= 80:
    print 'License and registration please'
    if mood == 'terrible' or speed >= 100:print 'You have the right to remain silent.'
    elif mood == 'bad' or speed >= 90:print "I'm going to have to write you a ticket."
