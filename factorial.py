# calculate the factorial of a given number

# ex: 7 = 7*6*5*4*3*2*1

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    # pass


# def factorialTrailingZeros(number):
#     pass
if __name__ == '__main__':
    # every module in python has a special attribute
    # called __name__attribute is set to__main__
    # When module run as main program. otherwise the value of
    # __name__ is set to contain the name of the module
    print("hello world")
    # if __name__ == "__main__":
    #     main()
    #     print("hello world")
    # when you execute main function it will the read if statement
    # and check whether __name__ does equal to __main__
    number: int = int(input("enter a number"))
    fac = factorial(number)
    print(f"The factorial is {fac}")
