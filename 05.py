x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

temp = x
x = y
y = z
z = temp

print("Values after rotation:",x,y,z)