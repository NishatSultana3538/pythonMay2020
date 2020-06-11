# I want to know even and odd numbers
# I also want to know if I divide the number by 10

num = int(input("give me a number to check: "))

check = int(input("give me a number divide by: "))

# if num % 4 == 0:
#     print(num, "is a multiple of 4")
#
# elif num % 2 == 0:
#     print(num, "is an even number")
#
# else:
#     print(num, "is an odd number")
# part2
if num % 4  == 0:
    print(num,"is a multiple of 4")

elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num,"is an odd number")

# part3

if num % check == 0:
    print(num, "is an even number", check)

else:
    print(num,"does not divide evenly by", check)