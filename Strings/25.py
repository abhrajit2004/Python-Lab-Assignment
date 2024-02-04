s = input("Enter a string: ")
substrings = []

for length in range(len(s)):
    for index in range(len(s)-length):
        substrings.append(s[index:index+length+1])

print(substrings)