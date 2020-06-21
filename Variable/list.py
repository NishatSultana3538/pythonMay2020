l = [1, "hi", "python", 7000 , 2, 876, 9766, "hello", 'hi']
print(l[3:])
print(l[0:2])
print(l)
print(l + l)
print(l * 3)
l.append(66)
# l.add(5678)
print(l)
l.insert(98000 , 'hello world')#98000 not printed
# l.insert(98000 , 'hello world',899)#dont take 3
print(l)
l.pop(2)#position 2 values removed
# l.pop( 2:5)#range not possible
print(l)
l.reverse()#reverse the list
print(l)
l.remove(7000)#remove one at a time
# l.remove(7000,876)#remove() takes exactly one argument (2 given)
print(l)
l.clear()#clear the whole list
# l.clear(5)clear() takes no arguments (1 given)
print(l)


#l.copy(3)
#print(l)
#l.sort()#sorting not possible if there is str and int mix
# print(l)

# Lists are similar to arrays in C. However; the list can contain data of different types. The items stored in the list are separated with a comma (,) and enclosed within square brackets [].
# We can use slice [:] operators to access the data of the list. The concatenation operator (+) and repetition operator (*) works with the list in the same way as they were working with the strings.
