#Calculate miles per gallon
print("This program calculates MPG")
# GET MILES DRIVEN FROM THE User
miles_driven = input("Enter miles driven:")
# convert text entered to a floating point number
miles_driven = float(miles_driven)

# get gallons used from the user
gallons_used = input("Enter gallons here: ")
# convert text entered to a in point number
gallons_used = int(gallons_used)

# calculate and print the answer
mpg = miles_driven/gallons_used

print("Miles per gallon:", mpg)


