string = "Hello,World!"
character_counts = {}

for char in string:
    if char not in character_counts:
        character_counts[char] = 1
    else:
        character_counts[char] += 1

print("The character counts are:",character_counts)