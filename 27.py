numbers = [12, 65, 54, 39, 102, 37, 72, 33, 5, -28, 0, 15]
max = numbers[0]
min = numbers[0]

for num in numbers:
    if num>max:
        max = num
    elif num<min:
        min = num

print("The maximum value in the list is:",max)
print("The minimum value in the list is:",min)