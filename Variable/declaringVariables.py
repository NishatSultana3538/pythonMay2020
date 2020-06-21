# Variable also known as identifier and used to hold value.
# In Python, we don't need to specify the type of variable because Python is a type infer language and smart enough to get variable type.

a = 10
name = 'Nishat'
salary = 100000.99
print(a)
print(name)
print(salary)
# multiple assignment
# Assigning single value to multiple variables

x = y = z = 50
print(x)
print(y)
print(z)

# Assigning multiple values to multiple variables
a, b, c = 5, 10, 15
print(a)
print(b)
print(c)


# Python does not bound us to declare variable before using in the application. It allows us to create variable at required time
# The first character of the variable must be an alphabet or underscore ( _ ).
# All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore or digit (0-9).
# Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).
# Identifier name must not be similar to any keyword defined in the language.
# Identifier names are case sensitive for example my name, and MyName is not the same.
# Examples of valid identifiers : a123, _n, n_9, etc.
# Examples of invalid identifiers: 1a, n%4, n 9, etc.