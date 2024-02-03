sum = 0
count = 1
while True:
    userInput = input("Enter the item price or press q to quit: ")
    f = open("receipt.txt","a")
    if userInput != 'q':
      sum = sum + int(userInput)
      print(f"Order total so far {sum}")
      f.write(f"{count}.{userInput}\n")
      count = count + 1
    else:
       print(f"Your Total Bill is {sum}. Thanks for shopping with us")
       break

f.close()