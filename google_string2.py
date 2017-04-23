#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  l = len(s)
  a = s[-(l-(l - 3)):]
  if l >= 3:
    if a != 'ing':
        s = s + 'ing'
    else:
        s = s + 'ly'
    return s
  else:
    return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  fir_not = s.find('not')
  sec_bad = s.find('bad')
  substr = s[fir_not:sec_bad+3]
  if sec_bad > fir_not:
      spt = s.replace(substr, 'good')
      return spt
  else:
      return s

def s_first_back(name):
    l_c = len(name)
    if l_c % 2 == 0:
        half = l_c / 2
        fir_half = name[ : half]
        sec_half = name[-half : ]
        return fir_half+','+sec_half
    else:
        l_c = (l_c + 1) / 2
        fir_half = name[ : l_c]
        sec_half = name[-(l_c-1) : ]
        return fir_half+','+sec_half


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    myList = []
    fir = s_first_back(a)
    sec = s_first_back(b)
    fir = fir.split(',')
    sec = sec.split(',')
    myList.insert(0, fir[0])
    myList.insert(1, fir[1])
    myList.insert(2, sec[0])
    myList.insert(3, sec[1])
    return myList[0]+myList[2]+myList[1]+myList[3]


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
