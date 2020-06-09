#Dreating a normal dictionary
'''d={"a":1,"b":2}
print(d["a"]);print(d["b"])
print(d["c"]) #will raise a key error since the given key that is "c" doesn't exist in the given dictionary d
#From above we conclude that normal or regular dictionaries will raise a key error if the entered key doesn't exist in the given dictionary
#Here comes the explanation and advantage of defaultdict as explained below
'''


'''defaultdict is a dictionary-like object which provides all methods provided by a dictionary but takes a first argument (default_factory) 
as a default data type for the dictionary. Using defaultdict is faster than doing the same using dict.set_default method.
A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.'''

from collections import defaultdict
'''d1={}
d1=defaultdict(object)
print(d1["one"]) #even though the dictionary d1 is empty and doesn't contain any key like "one" it won't raise any key error instead
# it will assign the value th the object passed inside the defauldict for this purpose
d1={"one":1,"two":2}
d1=defaultdict(object)
print(d1["one"]);print(d1["two"])
print(d1["three"])
for item in d1:
    print(item)
'''


'''
d2=defaultdict(lambda :0)
print(d2["I"])
print(d2["i_am_nothing"])
'''


'''d3=defaultdict(lambda :2)
print(d3[1])
for k,v in d3.items():
    print(k,",",v)
'''

