# !/usr/bin/env python
# coding: utf-8
# author:    bigbang
# date&time: 16/7/4 23:07


def displayNumType(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!'

if __name__ == '__main__':
    while True:
        num = input("input a number:")
        displayNumType(num)

