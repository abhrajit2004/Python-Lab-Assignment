string1 = input("Enter a string: ")
stringL1 = list(string1).sort()
string2 = input("Enter another string: ")
stringL2 = list(string2).sort()

if stringL1 == stringL2:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")