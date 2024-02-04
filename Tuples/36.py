numbers = (1, 2, 2, 3, 4, 4, 5, 6, 6, 6)
unique_numbers = []
duplicate_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
    elif num not in duplicate_numbers:
        duplicate_numbers.append(num)

print("The unique elements are:",tuple(unique_numbers))
print("The duplicate elements are:",tuple(duplicate_numbers))