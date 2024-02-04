list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = [x for x in list2 if x not in list1]

print("The numbers present in",list2,"but not in",list1,"are:",result)