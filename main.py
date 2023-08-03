import Stats

print("veuillez entrer les 5 notes :")
mylist = []
for i in range(5):
    mylist.append(float(input()))

print(Stats.somme(mylist))

print(Stats.moyen(mylist))

print(Stats.varience(mylist))