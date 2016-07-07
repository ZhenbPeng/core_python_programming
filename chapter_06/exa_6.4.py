# coding: utf-8
# author: pengzb
# date: 2016/7/7 11:21

queue = []


def enQ():
    queue.append(raw_input("Enter new string: ").strip())


def deQ():
    if len(queue) == 0:
        print "Cannot pop from an empty queue!"
    else:
        print "Removed ['%s']" % queue.pop(0)


def viewQ():
    print queue


CMDs = {
    'e': enQ,
    'd': deQ,
    'v': viewQ,
}


def showmenu():
    pr = """(e)nqueue
(d)equeue
(v)iew
(q)uit
Enter choice:"""

    while True:
        try:
            choice = raw_input(pr).strip()[0].lower()
        except (EOFError, KeyboardInterrupt, IndexError):
            choice = 'q'

        print "\nYou picked: [%s]" % choice

        if choice not in "edvq":
            print "Invalid option, try again"
            continue
        else:
            pass

        if choice == 'q':
            break

        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
