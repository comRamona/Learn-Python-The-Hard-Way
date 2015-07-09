__author__ = 'rami'
formatter="%r %r %r %r"
print formatter %(1,2,3,4)
print formatter %(True,False,False,True)
print formatter % (formatter, formatter, formatter, formatter)