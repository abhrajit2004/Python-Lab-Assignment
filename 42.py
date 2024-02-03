cricket = {}
n = int(input("Enter the number of players: "))
for i in range(n):
    name = input("Enter the name of the player "+ str(i+1) + ": ")
    runs = int(input("Enter the runs scored by "+ name +": "))
    cricket[name] = runs

name = input("Enter a player's name: ")
if name in cricket:
    print("The runs scored by",name,"are:",cricket[name])
else:
    print("-1")