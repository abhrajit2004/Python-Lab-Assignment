p = int(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = int(input("Enter duration: "))

i = (p*r*t)/100
total = p + i

print("The interest amount will be:", i)
print("The total amount will be:", total)