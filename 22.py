s = input("Enter a string: ")
s = s.lower().replace(" ","")

r = s[::-1]

if r==s:
    print("It is a palindrome")
else:
    print("It is not a palindrome")