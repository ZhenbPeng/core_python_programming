# !/usr/bin/env python
# coding: utf-8
# author:    bigbang
# date&time: 16/7/4 21:32


""" readTextFile.py -- read and display text file
"""


fname = raw_input("Enter filename: ")
print

try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open error:", e
else:
    for eachLine in fobj:
        print eachLine,
    fobj.close()
