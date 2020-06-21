# List contain items of different data types. Lists are mutable i.e., modifiable.
# The values stored in List are separated by commas(,) and enclosed within a square brackets([]). We can store different type of data in a List.
# Value stored in a List can be retrieved using the slice operator([] and [:]).
# The plus sign (+) is the list concatenation and asterisk(*) is the repetition operator.

list=['aman',678,20.4,'saurav']
list1=[456,'rahul']
print(list)
# ['aman', 678, 20.4, 'saurav']
print(list[1:3])
# [678, 20.4]
print(list+list1)
# ['aman', 678, 20.4, 'saurav', 456, 'rahul']
print(list1*2)
# [456, 'rahul', 456, 'rahul']