#Functions can return something 

def add(a,b):
	print "ADDING %8.2f + %.2f" %(a,b)
	return a+b

def substract(a,b):
	print "SUBSTRACTING %8.2f - %.2f" %(a,b)
	return a-b

def multiply(a,b):
	print "MULTYPLYING %8.2f * %.2f" %(a,b)
	return a*b

def divide(a,b):
	print "DIVIDIING %8.2f / %.2f" %(a,b)
	return a/b

age=add(14,5)
weight=substract(50,2.3)
height=multiply(2.5,3)
iq=divide(101,2)

print "Age: %.2f, Height: %.2f, Weight: %.2f, IQ: %.2f" %(age,height,weight,iq)

print "Something cool:"
sth=add(age,substract(height,multiply(weight,divide(iq,2))))
print sth
a=int(raw_input("What is your age?\n>"))
b=int(raw_input("What is your iq?\n>"))
c=substract(b,a)
print ("Your age is %d smaller than your iq.\nThat's preeetty close "
        "mate." %c)


