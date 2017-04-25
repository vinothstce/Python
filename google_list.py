from audioop import reverse
a = [1, 2, 3, 4, 5]

#Adding two items to the list will simply add them as like string
print a + [2, 5]

#Below things say that when a list is  copied using a = b the same is not actually copied there is only one list referred by two variable
b = a

a[0] = 13
print a 

print b

#In case copy is needed then do the below things to make  a copy
c = a[:]

a[1] = 12

print a 
print c

#To iterate a loop and print each and every item in a loop is by below things
for i in a:
    print i

# single statement checking in python
# value in list
d =  12 in a
print d


#append does not return any thing it just modifies the list
a.append(10)
print a

a = a.append(12) # Statement like this is wrong as append will not return any thing it just modifies the list and statement like this will make a as None which is same as null


print a # This returns None which is same as null

#pop statement just remove the element from the list and returns the same
print b
print b.pop(1)
print b

#del statement remove particular variable or defined thing in the del statement from the memory and not the source or source list or other variable pointing to the same list

d = 12
e = [1, 2, 3, 4, 5]

f = d
g = e
del d 
del e

print f
print g

#Below things will print error as the same is deleted so it is commented
#print d
#print e

#sorted method will make a copy of original thing and sort things in a increased order
h = [5, 2, 8, 1, 4]
print sorted(h)

help(sorted)

#Below are the example's of custom sorting

# Below thing will sort the item but in reverse order
print sorted(h, reverse = True)

def Last(s):
    return s[-1]

#Below thing will inform sorted to make a copy and compare using len method by creating a shadow list
#len('bbb')-->3 len('cc')-->2 len('aaa')-->3 len('dddd')-->4
i = ['b', 'cc', 'aaaz', 'dddd']
print sorted(i)
print sorted(i, key=len)

#Say for eg. we are interested in sorting based on last character of the string then we will use

print sorted(i, key=Last)

#join method takes a list and concatenate items in a list with a specific character
print ':'.join(i)

#split do the opposite thing of a list
b = ':'.join(i)
a = b.split(':')
print a 

#Accessing each item in a list
for x in i:
    print x
    
print 'cc' in i

#Accessing a list and put the same in other list
result = []
for y in i:
    result.append(y)

print result

#range method will built the list on the fly, which can be used as like normal for loop in other programming language
#Below things actually saves memory
print range(20)
for z in range(20):
    print z

#Tuples & sting are immutable but list is mutable is puts in parenthesis with commas separated, which is saving a fixed number of things 
#All methods and things like accessing array apply to tuple a[0], b[2] etc except tuple is immutable that's it can't be modified

a = (1, 2, 3)
# a[0] = 13 # This statement will display an error

# In case needed to sort a thing based on two things use the below one
# Below thing will look for first element in a tuple in case first element of two tuple are same then sorting will be based on second element, 
# 

a = [(1, "b"), (2, "a"), (1, "a")]

print sorted(a)

#Tuple can be used for parallel assignment
(x, y) = (1, 2)
print x
print y


