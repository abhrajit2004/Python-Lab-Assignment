vowels = ['a','e','i','o','u']

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
countVwl = [0, 0, 0, 0, 0]

for char in sentence:
    if char in vowels:
        countVwl[vowels.index(char)] += 1

print("The number of vowels in the sentence is",countVwl)