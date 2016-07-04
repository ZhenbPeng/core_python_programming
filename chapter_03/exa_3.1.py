# !/usr/bin/env python
# coding: utf-8
# author:    bigbang
# date&time: 16/7/4 21:32

'''makeTextFile.py -- create text file'''

import os
ls = os.linesep

while True:
    fname = raw_input("Please input a file name:")
    if os.path.exists(fname):
        print "ERROE: '%s' already exists" % fname
    else:
        break

lines = []
print "\nEnter lines ('.'by itself to quit).\n"

while True:
    entry = raw_input("> ")
    if entry == '.':
        break
    else:
        lines.append(entry)

fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in lines])
fobj.close()
print 'DONE!'
