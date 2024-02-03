vowels = ['a','e','i','o','u']
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
count = [0,0,0,0,0]
for char in sentence:
    if char in vowels:
        count[vowels.index(char)] += 1
print(count)
