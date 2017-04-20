import sys

def Hello(name):
    if name == 'Alice' or name == 'Nick':
        name = name + '???'
    else:
        DoesNotExist(name)
    name = name + '!!!'
    print(name)
        
def main():
    Hello(sys.argv[1])
    
if __name__ == '__main__' :
    main()