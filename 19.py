num = 0
count_of_prime = 0
count_of_composite = 0

while num!=-1:
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                count_of_composite += 1
                break
        else:
            count_of_prime += 1

print("The count of prime numbers is:",count_of_prime)
print("The count of composite numbers is:",count_of_composite)