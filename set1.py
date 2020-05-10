thisset = {"1", "4", "9","8"}
# thisset1 = {"7", "2", "3", "5"}
thisset1 = {"7", "a", "b", "c"}

thisset2 = {"a", "d", "e"}
# thisset2 = {"a", "d", "c"}
# thisset.remove("2")
# thisset.discard("3")
print(thisset)
print(thisset1)
# what if i want a,b,c in thisset???
set3 = thisset.union(thisset1)
print(set3)
set4 = set3.union(thisset2)
print(set4)