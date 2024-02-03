sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
words = sentence.split()
count = 0

for i in words:
    if i==word:
        count += 1

print("The word", word, "occurs", count, "times in the sentence")