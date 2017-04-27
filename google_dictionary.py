import sys
from test.test_readline import readline

# dictionary are declared within {} open and close curley braces
d = {}
d['a'] = 'alpha'
d['o'] = 'omega'
d['g'] = 'gamma'


print d
print d['a']
d['o'] = 6
print d
print 'a' in d

if 'z' in d: # This statement will return false
    print d['z'] #Throws KeyError
    print d.get('z')#None (instead of KeyError)


#To get the values of the dictionary use like below,
print d.get('a')
print d.get('x')

#To Check whether a key is there in the dictionary use as like below,
print 'a' in d
print 'x' in d

#To get all the keys and values in the dictionary use as like below,
print d.keys()
print d.values()


#To access the keys and values in the dictionary use as like below things
for k in sorted(d.keys()):
    print 'key :', k, 'values :-->', d[k]

#To get items in a tuple use like below with key and values in each tuple
print d.items()

#To access the tuple in d.items() use below things,
for tuple in d.items():
    print tuple

#Use a Dictionary to figure out ip address of the system that is hitting my server by looking at the log files
#Using ip address as key and counting the value i.e increamenting the same when a particular ip hit the server

#Instead of 'r', use 'w' for writing, and 'a' for append.
#File open method in details
comment_py = """
The first argument of open is the filename. The second one (the *mode*) determines *how* the file gets opened.

– If you want to read the file, pass in r
– If you want to read and write the file, pass in r+
– If you want to overwrite the file, pass in w
– If you want to append to the file, pass in a
"""

# First python way of reading a text file with below commands
 
comment_py = """
# Open a file and read the same
def Cat(filename):
    f = open(filename, 'rU') #rU to read a file and ignore dos line endings and unix line endings
    #next(f) #Use this statement in case first line is not needed
    for line in f: #This statement will read the file line by line and print the same, line string include a new line at the end  
        print line, #print line will print the same including a new line character at the end  
    f.close() # Use this statement to close the file, in case not used then it will be closed by default 
    """
        
comment_py = """  
# Second way to reading a text file with below commands
def Cat(filename):
    f = open(filename, 'rU')
    lines = f.readlines()# This statement will read all line in a file and put that in a list
    #line = f.readline() # This will read only a single line from the file and print the same 
    #print line + "Hello"
    print lines
    f.close()
    #Includes the new line at the end which can be avoided or delimited by adding comma at the end
    """
comment_py = """
# The third way of reading a file is with below things
def Cat(filename):
    f = open(filename, 'rU')
    text = f.read()
    print text
    f.close()
    """
#To make sure that the file gets closed whether an exception occurs or not, pack it into a with statement:
def Cat(filename):
    with open(filename, 'rU') as f:
        text = f.read()
    print text
    f.close()

if __name__ == '__main__':
    Cat(sys.argv[1])