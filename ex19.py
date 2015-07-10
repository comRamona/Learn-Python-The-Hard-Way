def cheese_and_crackers(cheese,crackers):
	print ("You have %d cheeses and %d crackers.\nMan, "
           "that's enough for a partyyeah!" %(
            cheese, crackers) )

print "How much food?"
cheese_and_crackers(30,30)

print "What if I eat some?"
ch=30
cr=30
eat=15
cheese_and_crackers(ch-eat,cr-25)
