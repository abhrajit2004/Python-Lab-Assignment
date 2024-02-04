numbers = (1, 2, 3, 4, 5, 6)
even_numbers = [x for x in numbers if x%2 == 0]
result = []

for i in range(len(even_numbers)):
    for j in range(i+1, len(even_numbers)):
        result.append((even_numbers[i],even_numbers[j]))

print("The distinct pairs from the list", numbers,"are:", result)