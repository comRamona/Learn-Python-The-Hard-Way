print "How old are you?",
age=int(raw_input())  #get user input
print "How tall are you?",   #use comma to get answer on the same line
height=raw_input()
print "How much do you weigh?",
weight=raw_input()

print "I am a fortune teller and I can say you're %d years old, %s tall and %s heavy." %(
    age,height,weight)

age10=age+10

print "In 10 years you will be %d, I hope you will be prettier by then." %age10

q=raw_input("Give me an idea for a question:")
ans=raw_input("OK, tell me %s and stuff: " %q)
print "Thanks for saying %s!"%ans

print ("I can break up "
         "lines like this")



