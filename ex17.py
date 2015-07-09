from sys import argv
from os.path import exists

script, from_file, to_file=argv

print "Copying from file %r to file %r" %(from_file,to_file)

in_file=open(from_file)
data=in_file.read()

print "The input file is %d bytes long" %len(data)

print "Does the output file exists? %r" %exists(to_file)
print "Ready, hit ENTER to continue, CTRL-C to abort."
raw_input()
out_file=open(to_file,'w')
out_file.write(data)

print "All right, all done."

in_file.close()
out_file.close()
