from __future__ import print_function
import sys
# File Objects
comment_python = """
f = open('test.txt', 'r')
#To print the name of the file
print(f.name)

#To print the mode of the file
print(f.mode)
f.close()
"""


#There is a possibility for error in opening a file so close statement after that won't be called so use statement as below for close file even in case of error
#context manager as below is the best practice as the same will close file in case of any error and no close statement is needed 
with open('test.txt', 'r') as f:
    print(f.name)
#Below statement is the validation for closing the file
print(f.closed)

#Reading and printing all the content of the file 
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    
#Reading all lines of the file in a list is by below things
with open('test.txt', 'r') as f:
    f_readlines = f.readlines()
    print(f_readlines)
    
#Reading only the first line of the file
with open('test.txt', 'r') as f:
    f_readline = f.readline()
    print(f_readline)
    
    f_readline = f.readline()
    print(f_readline)
    
#First way to remove the empty line between statements is by
with open('test.txt', 'r') as f:
    f_readline = f.readline()
    print(f_readline,)
    
    f_readline = f.readline()
    print(f_readline,)
    
    
    print(sys.version)

#Second way to remove the empty line between statements is by
with open('test.txt', 'r') as f:
    f_readline = f.readline()
    print(f_readline, end='')
    
    f_readline = f.readline()
    print(f_readline, end='')

#Reading all content of a file in an efficient way
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

#Reading in a better way
with open('test.txt', 'r') as f:
    f_contents = f.read(100) #This statement will read the first 100 characters of the file
    print(f_contents, end='')
    
    f_contents = f.read(100) #This statement will read the first 100 characters of the file
    print(f_contents, end='')
    
    #Below thing will return an empty string as there is no content to print after the above statement
    f_contents = f.read(100) #This statement will read the first 100 characters of the file
    print(f_contents, end='')
    
#Reading above in more better way
with open('test.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read) 
    
#Reading in another way
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
           
#To find out the current position of the file use as like below,
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    
    print(f.tell())
    
#To move to beginning of the file while reading is by below things, to move to particular position in a file use f.seek(position)
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)
    
    f.seek(0)
    
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)
#On writting in case the file 
comment_python = """

1. In case file is not existing then it will create a file and write on the same, 
2. In case file exist then it will ovverride on same
3. In case we are interested in just adding content to the file then use append 
"""
#Writting in a file using read in open command will thow an error IOError: File not open for writing
with open('test.txt', 'r') as f:
    #f.write('Hello')
    pass
    
#Writting to a file in a proper way
with open('test2.txt', 'w') as f:
    f.write('Test')    
#Overriding an existing file is by below,
with open('test2.txt', 'w') as f:
    f.write('Hello')
#To append to an existing file use as below,
with open('test2.txt', 'a') as f:
    f.write('Test')
    
# Using file seek in a efficient way for overriding needed things in the file things to a file
with open('test2.txt', 'w') as f:
    f.write('Hello')
    f.seek(0)
    f.write('R') 
    
#Reading a content from a file and writting the same to a new file
with open('test.txt', 'r') as rf:
    with open('test2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

comment_python = """            
#Reading a jpeg file use below things for reading an image which is reading a bytes and using binary mode rather than reading a text files
with open('cat.JPG', 'rb') as rf:
    with open('cat1.JPG', 'wb') as wf:
        for line in rf:
            wf.write(line)
            """
#Reading in more efficient way as before
with open('cat.JPG', 'rb') as rf:
    with open('cat1.JPG', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        f_contents = rf.read(chunk_size)
        while len(f_contents) > 0:
            wf.write(rf_chunk)
            f_contents = rf.read(chunk_size)