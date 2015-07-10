def print_two(*args):
     x,y=args
     print x,y

def print_twoagain(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1,arg2)

def print_one(arg):
	print arg

def print_three(x,y,z):
	print x,y,z

def print_nothing():
    print "I've got nothing"

print_two("me","Potato")
print_twoagain(3,4)
print_one("Columb")
print_nothing()  #well actually nothing means no arguments
print_three(00,10,11)
	
