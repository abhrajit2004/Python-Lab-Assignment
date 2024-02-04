# Using third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a
a = b
b = c
print("Values after swapping:", a,b)

# Without using third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("Values after swapping:", a,b)