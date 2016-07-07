# coding: utf-8
# author: pengzb
# date: 2016/7/7 17:38

db = {}


def newuser():
    prompt = "login desired:"
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = "name taken, try another: "
            continue
        else:
            pass

        pwd = raw_input("passwd: ")
        db[name] = pwd
        return

def olduser():
    name = raw_input("login:")
    pwd = raw_input("passwd:")
    passwd = db.get(name)
    if passwd == pwd:
        print "welcome back", name
    else:
        print "login incorrect"


CMDs = {
    'n': newuser,
    'e': olduser,
}

def showmenu():
    prompt = """(n)ew user login
(e)xisting user login
(q)uit
Enter choice:"""

    while True:
        try:
            choice = raw_input(prompt).strip()[0].lower()
        except (EOFError, KeyboardInterrupt, IndexError):
            choice = 'q'
        print "\nYou picked:[%s]" % choice

        if choice not in 'neq':
            print "invalid option, try again"
        else:
            if choice == 'q':
                return
            CMDs[choice]()

if __name__ == '__main__':
    showmenu()
