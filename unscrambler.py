#!/usr/bin/python

import enchant
import sys
import itertools
import array

# Define function for checking for priority words.
def priorityFunction(s, p):
    l = len(p)
    for i in p:
        if i not in s:
            return False
    return True
    
# Setup dictionary.
d = enchant.Dict("en_US")

# Setup list of unadmittable characters.
delchars = ''.join(c for c in map(chr, range(256)) if not c.isalpha())

# Print openning message.
print ""
print "     ~`*-- Welcome to the Unscrambling Machine! --*'~"    
print "This  program  will take a string you enter and  check  for"
print "all possible English words. Incorrect input such as special"
print "characters  and  numbers  will be removed  before  testing."
print ""

ans = 'y'

while(ans == 'y'):
    # Receive user input.
    sword = raw_input("Enter a string of letters to be unscrambled: ")
    pchar = raw_input("Enter a string of priority letters or 0 for none: ")
    print ""

    # Format user input.
    sword = sword.translate(None, delchars)
    sword = sword.lower()  
    pchar = pchar.translate(None, delchars)
    pchar = pchar.lower()

    x = []          # Initiate list to receive permutations of input characters.
    check = []      # Initiate list to receive one dimensional array of permutations.
    good = []       # Initiate list to receive array of words.
    priority =[]    # Initiate list to receive array of priority words.

    # Create all possible permutations of input letters.
    for index in range(2, len(sword)):
        x.append(list(itertools.permutations(sword, index+1)))
    
    # Create a one dimensional array of the permutations.
    for index in range(len(x)):
        for i in x[index]:
            check.append(''.join(i))
    
    # Check permutations against dictionary, add to good or priority list if a word.    
    for index in range(len(check)):
        if d.check(check[index]) == True:
            if check[index] not in good:
                good.append(check[index])

    # Check good list for priority words. Add priority words to priority list and remove from good.
    if len(pchar) > 0:
        for index in good:
            if priorityFunction(index, pchar) == True:
                priority.append(index)

    for index in priority:
        good.remove(index)
    
    # Format lists for printing.
    while len(priority)%3 !=0:
        priority.append(' ')
    while len(good)%3 !=0:
        good.append(' ')

    # Print lists.
    if len(priority) > 0:    
        print "Priority words: "    
        for a,b,c in zip(priority[::3], priority[1::3], priority[2::3]):
            print '{:<20}{:<20}{:<}'.format(a,b,c)   
        print ""
    else:
        print "Sorry, no priority words found."
        print ""

    if len(good) > 0:
        print "All other found words: "    
        for a,b,c in zip(good[::3], good[1::3], good[2::3]):
            print '{:<20}{:<20}{:<}'.format(a,b,c)
        print ""
    else:
        print "Sorry, no other words found."
        print ""
    
    # Check if user wants another string unscrambled.
    ans = raw_input("Enter 'y' if you wish to start again, else program will exit: ")
    ans = ans.lower()
    print ""