numbers = input("Please enter a sequence of comma-separated numbers: ")
numbers_list = numbers.split(',')
numbers_list = [int(num) for num in numbers_list]
numbers_tuple = tuple(numbers_list)
print("The tuple is:",numbers_tuple)