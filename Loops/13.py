a = int(input("Enter the lower range: "))
b = int(input("Enter the upper range: "))

for i in range(1, a+1 if a>b else b+1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("GCD of",a,"and",b,"is",hcf)