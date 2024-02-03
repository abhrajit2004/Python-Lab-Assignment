sen = input("Enter a sentence:")
word = input("Enter a word:")
words = sen.split()
count = 0
# print(words)
for i in words:
    if i == word:
        count += 1
print(count)
print("The word",word,"occurs",count,"times in the sentence")