t1 = 0
t2 = 1
sum = 0
for i in range(3, 13):
    t3 = t1+t2
    if t3 % 2 == 0:
        sum += t3
    t1 = t2
    t2 = t3

print("The sum of the even-valued terms of the fibonacci series upto 100 is",sum)