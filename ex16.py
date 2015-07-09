from sys import argv

script,filename=argv

print ("We're going to erase %r.\n If you don't want that, hit CTR-C (^c). \n "
     "If you do want that,  hit Enter.") %filename

raw_input("?")
print "Opening the file.."
target=open(filename,'w')

print 'File has been truncated'
print 'Now I\'m going  to ask you for three lines.'

line1=raw_input("line 1: ")
line2=raw_input("line 2: ")
line3=raw_input("line 3: ")

print "Now I am goint to write there to the file."

target.write(line1+
    "\n"+line2+"\n"+line3+"\n")

print "And finally, we close it."
target.close()

#open accepts arguments:
# w: open for writing. truncates the file and creates a new one if it does not exist
# a: append at the end of file
# r: read
# a+: append and read
# w+: write and read, truncate
# r+: write at the beginning and read
