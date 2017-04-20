# Variables are immutable meaning assigned value once that are not modified 
#Place holder for variable inside a string
a = 'Hello'
a = "Hello"


print(a + 'yay!')
print(a) 

print(a.lower())
print(a.find('e'))
print(a[1])
print(a[2])
#Hello
#01234
#-5-4-3-2-1

#a[start:end neglecting end]
#Starting at one but not including 3
print(a[1:3])

print("Hi %s i have %d donuts" % ('Alice', 42))

#Below thing starts from beginning and go till 4
print(a[:4])

#Below thing starts from 1 and go till the end
print(a[1:])

#Below thing starts from beginning till the end
print(a[:])

#Minus indicates from last but syntax remain the same
 
print(a[-4:-2])

#Below things will start from beginning and end at before 'l' i.e neglecting 'l'
print(a[:-3])

#Below thing will print starting from 'l' till end
print(a[-3:])