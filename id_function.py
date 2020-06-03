c=10
print(id(c))
print("Return type of the id() function is:",type(id(c)))
print(id(108))
print(type(id(108)))
def add(a,b):
    c=a+b
    return c
z=add(4,4)
print("The result of function add(4,4) is",z)
print("The result of the above add(4,4) function is stored at address:")
print(id(z))
print(id(add(4,4)))