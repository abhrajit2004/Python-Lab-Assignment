l = int(input("Enter the lower range: "))
h = int(input("Enter the upper range: "))
sum = 0
for num in range(l, h+1):
    if num>1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            sum += num

print("The sum of all prime numbers between",l,"and",h,"will be:",sum)