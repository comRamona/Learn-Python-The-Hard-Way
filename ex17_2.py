from sys import argv
from os.path import exists

script, from_file, to_file=argv


#one line version for copying a file:

open(to_file,'w').write(
     open(from_file).read())



