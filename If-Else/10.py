p = int(input("Enter principal amount: "))
t = int(input("Enter duration: "))

if p<200000:
    r = 10

elif p>=200000 and p<=1000000:
    r = 12

else:
    r = 15

i = (p*t*r)/100

print("The rate of interest is:",r)
print("The simple interest will be:",i)