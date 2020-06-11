with open('currencydatatype.txt') as f:

    # a = f.readlines()

    # print(a)

# with open('currencydatatype') as f:
#
#     a = f.readlines()
#
#     print(a)
    lines = f.readlines()
    print(lines)

    for line in lines:
        parsed = line.split("\t")
        print(parsed)
        break
        lines = f.readlines()

    print(lines)

    currencyDict = {}
    for line in lines:
        parsed = line.split("\t")
        currencyDict[parsed[0]] = parsed[1]
        # print(parsed)
        print(currencyDict)
        # break
        # break
        # amount = input("Enter amount:\n")
        # amount = int(input("Enter amount:\n"))
    amount = float(input("Enter amount:\n"))
    print("Enter the name of currency you want to convert this amount to?Available option\n")
    [print(item) for item in currencyDict.keys()]
    currency = input("please enter one of the values")
    print(f"{amount} USD is equal to {amount *float(currencyDict[currency])}{currency}")