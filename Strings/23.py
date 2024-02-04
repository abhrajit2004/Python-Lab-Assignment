s = input("Enter a string: ")
s = s.lower()
last_char = s[-1]
new_string = s[:-1].replace(last_char, '*') + last_char
print("New string:", new_string)