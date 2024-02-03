numbers = (1, 2, 2, 3, 4, 4, 5, 6, 6, 6)
frequencies = {}

for num in numbers:
    if num not in frequencies:
        frequencies[num] = 1
    else:
        frequencies[num] += 1

print("The frequencies are:",frequencies)