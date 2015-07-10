from sys import argv

script,input_file=argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
    print line_count," : ", f.readline()

cfile=open(input_file)

print "I will first print the whole file:\n"
print_all(cfile)

print "Let's go back"
rewind(cfile)

print "Let's print three lines\n"
print_a_line(1,cfile)
print_a_line(2,cfile)
print_a_line(3,cfile)

print "Let's print the first line again\n"
rewind(cfile)
print_a_line(1,cfile)
