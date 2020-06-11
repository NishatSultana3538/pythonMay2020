# write a python program which will keep adding a stream of numbers inputed by the
# users. the adding will stop as as user process q key on the keyboard
sum = 0
while(True) :
    # number = input("enter the price: \n")
    userInput = input("enter the price: \n")
    if (userInput != 'q') :
        sum = sum + int(userInput)
        print(f"Order total so far:{sum} ")
    else:
        print(f"Your total bill is {sum}.Thank you for shopping with walmart ")
        break

# keep adding number
# enter q for finish. will give the total bill.
# print("Thank you for visiting our store")
# print("")
# f= f-string is a literal string, the expressions are replaced with their values.