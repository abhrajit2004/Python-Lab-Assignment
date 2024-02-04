a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Numbers after sorting:")
if a<b:
    if b<c:
        print(a,b,c)
    elif a<c:
        print(a,c,b)
    else:
        print(c,a,b)
    
else:
    if c<b:
        print(c,b,a)
    elif c<a:
        print(b,c,a)
    else:
        print(b,a,c)