import math
def somme(mylist):
    c=0
    for a in mylist:
       c+=a
    return c

def moyen(mylist):
    c=0
    for a in mylist:
       c+=a
    return c/5

def varience(mylist):
    c=0
    for a in mylist:
       c+=(a-moyen(mylist))**2
    return c/ (len(mylist)-1)

def ecartType(mylist):
    return math.sqrt(varience(mylist))


