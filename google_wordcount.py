import sys
from audioop import reverse

def word_count_dict(filename):
    word_counts = {}
    input_file = open(filename, 'r')
    for line in input_file:
        words = line.split()
        for word in words:
            word = word.lower()
            #Special case if we are seeing this word for the first time
            if not word in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
    return word_counts

def helper(filename):
    word_counts = word_count_dict(filename)
    return word_counts 

def print_words(filename):
    word_counts = helper(filename)
    words = sorted(word_counts.keys())
    for word in words:
        print word, word_counts[word]   
    
    
def print_top(filename):
    word_counts = helper(filename)
    tuples = []
    for word in word_counts:
        tuples.append((word_counts[word], word))
        tuples = sorted(tuples, reverse=True)
        print sorted(tuples, reverse=True)
        print word, word_counts[word]
    i = 1
    for tuple in tuples:
        if i <= 20:
            print tuple[0], tuple[1]
            i += 1
        
comment_python = """
def print_words(filename):
    with open(filename, 'r') as rf:
        for line in rf:
            print line
            spWord = line.split()
            for word in spWord:
                print word
                count = spWord.count(word)
                print word+ ' '+count 
    """
comment_python = """
def print_words(filename):
    a = []
    with open(filename, 'r') as rf:
        f_contents = rf.read()
        sp_contents = f_contents.lower().split()
        print f_contents,
        print sp_contents
        for sp_content in sp_contents:
            count = sp_contents.count(sp_content)
            tuple = (sp_content, str(count))
            a.append(tuple)
            print sorted(a) 
            print sp_content + " " + str(count)



def print_words(filename):
    a = []
    with open('small.txt', 'r') as rf:
        wordcount = {}
        for word in rf.read().lower().split():
            if word not in wordcount:
                wordcount[word] = 1
                tuple = (word, wordcount[word])
            else:
                wordcount[word] += 1
                tuple = (word, wordcount[word])
            a.append(tuple)    
            print(word, wordcount)
            print tuple
        for key in wordcount.keys():
            print("%s %s" %(key, wordcount[key]))
"""            


if __name__=='__main__':
    print_words("small.txt")
    print_top("small.txt")
    
    