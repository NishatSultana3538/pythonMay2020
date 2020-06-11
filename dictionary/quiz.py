# create a dictionary and take input from the user and return the meaning of the word from the dictionary

# l1={"pranti": "burger", "priyana": "lemonhead", "tofael": "cars",
#      "Jimmy": "perfume", "Eva": "home", "jenifer":{"A": "kids",
#                                                        "B":"Burger","C":"chicken"}}
# l1 ["moh"] = "pizza"
# l1 ["rabia"] = "kebab"
# l1 ["vicky"] = "iphone"
# print(l1)
word = input("enter your word")
dict = {"ankur":"teacher","jimmy":"player","john":"pizzaman","pranti": "burger", "priyana": "lemonhead", "tofael": "cars",
   "Jimmy": "perfume", "Eva": "home", "jenifer":{"A": "kids",
                                                       "B":"Burger","C":"chicken"}}
print(dict[word])
searchword = input("enter your searchword")
dict = {"ankur":"teacher","jimmy":"player","john":"pizzaman","pranti": "burger", "priyana": "lemonhead", "tofael": "cars",
   "Jimmy": "perfume", "Eva": "home", "jenifer":{"A": "kids",
                                                       "B":"Burger","C":"chicken"}}
print(dict[searchword])