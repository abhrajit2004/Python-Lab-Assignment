list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

for x in list2:
    if x not in list1:
        list1.append(x)

print("Union of two lists is:",list1)