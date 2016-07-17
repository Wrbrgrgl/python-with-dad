#!python
""" playing with some basic inut and output """
import sys

# arguments = set(sys.argv)
# print "Passed in {} arguments, with {} unique ones, they are :".format(len(sys.argv)), len(arguments))
arguments = set()
print "Passed in {} arguments, they are:".format(len(sys.argv) - 1)
for arg in xrange(1, len(sys.argv)):
    arguments.add(sys.argv[arg])

print arguments
