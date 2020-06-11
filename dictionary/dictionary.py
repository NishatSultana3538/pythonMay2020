# dictionary is nothing but key value pairs, a dictionary is a collection of a unordered, changable and indexed

d1 ={}

#print(type(d1))

d2 ={"harry": "burger", "Arshad": "fish", "Nasir": "cars", "Jimmy": "perfume", "Kaitlin": "home", "jenifer":{"A": "kids", "B":"Burger","C":"chicken"}}
d2 ["moh"] = "pizza"
d2 ["rabia"] = "kebab"
d2 ["vicky"] = "iphone"
print(d2)

if "jimmy" in d2:
    print("yes,'jimmy' is one of the keys in the d2 dictionary")
# length
print(len(d2))
#method remove last item
d2.popitem()
print(d2)
#delete
#keys
del d2["jenifer"]#key level delete
print(d2)
#delete full program
# del d2- will delete the dictionary and give an error
print(d2)
# clear will delete entire dictionary and give ana empty one
# d2.clear()
# print(d2)

# copy
# d3 = d2.copy()
# print(d3)
d2.update({"harry": "coffe"})
# print(d2)
print(d2.get("harry"))

nested dictinary

user1 = {
    "user" :{
    "name" : "ankur",
    "year" : 1969
}

user2 ={
    name : "linus"
    "year" : "2004"
}

}