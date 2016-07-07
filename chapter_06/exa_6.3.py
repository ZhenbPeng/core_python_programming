# coding: utf-8
# author: pengzb
# date: 2016/7/7 10:52

stack = []


def pushit():
    stack.append(raw_input('Enter new string: ').strip())


def popit():
    if len(stack) == 0:
        print "Cannot pop from an empty stack!"
    else:
        print "Removed ['%s']" % stack.pop()


def viewstack():
    print stack

CMDs = {
    'u': pushit,
    'o': popit,
    'v': viewstack,
}

def showmenu():
    pr = \
"""p(u)sh
p(o)p
(v)iew
(q)uit
Enter choice:"""

    while True:
        try:
            choice = raw_input(pr).strip()[0].lower()
        except (EOFError, KeyboardInterrupt, IndexError):
            choice = 'q'

        print "\nYou picked: [%s]" % choice

        if choice not in "uovq":
            print "Invalid option, try again"
            continue
        else:
            pass

        if choice == 'q':
            break

        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
