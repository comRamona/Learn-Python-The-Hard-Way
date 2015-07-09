from sys import argv

script, filename=argv

txt=open(filename)

print "Here's your file %r:" %filename
print txt.read()

print "Type another filename:"
file_2=raw_input(">")

#a+ to append at the end
#r+ to append at the beginning and read from there

txt_2=open(file_2,"a+")
text_print=raw_input("give me something to append\n ")
txt_2.write(" "+text_print)

#important to close it hear so it is updated when you read again
txt_2.close()

txt_2r=open(file_2,"r")
print "New contents of the file:\n",txt_2r.read()

txt.close()

txt_2r.close()

#let's do it again

file_3=raw_input("Give me another file:")
txt_3=open(file_3,"a+")
print txt_3.tell()
txt_3.seek(0,0)
text_print3=raw_input("give me something to append\n ")
txt_3.write(text_print3)
print txt_3.tell()
txt_3.seek(0,0)
print "New contents of your last file:"
print txt_3.read()
txt_3.close()

# A from_what value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.
