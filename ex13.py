__author__='rami'
#command line arguments are stored in argv
#and then unpacked in script, first,second,third
#run as python ex13.py 1 2 3

from sys import argv

script, first, second, third=argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

ques=raw_input('Which of the variable do you want to change?')
print "Ok, we will change", ques


