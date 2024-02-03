s = input("Enter a string: ")
s = s.lower().replace(" ","")
r = s[:-1]
print(r)

if s == r:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
