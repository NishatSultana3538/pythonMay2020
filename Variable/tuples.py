# Tuple is another form of collection where different type of data can be stored.
# It is similar to list where data is separated by commas. Only the difference is that list uses square bracket and tuple uses parenthesis.
# Tuples are enclosed in parenthesis and cannot be changed.

tuple=('rahul',100,60.4,'deepak')
tuple1=('sanjay',10)
print(tuple)
print(tuple[2:])#range from position 2 untill end
print(tuple[3:])#range from position 3 untill end
print(tuple[1:])#range from position 3 untill end
print(tuple[:3])#range from position 0 to 3
print(tuple[1:3])#range from position 1 to 3
print(tuple[1:3:1])#range from position 1 to 3,by 1 increment

print(tuple1[0])

print(tuple+tuple1)
