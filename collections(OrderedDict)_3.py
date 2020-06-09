#Normal/regular dictionary
'''d={}
d["a"]=1
d["b"]=2
d["c"]=3
d["d"]=4
d["e"]=5
print(d)
for k,v in d.items():
    print("Key",k,"is associated with value",v)
#Output:
Key a is associated with value 1
Key b is associated with value 2
Key c is associated with value 3
Key d is associated with value 4
Key e is associated with value 5
'''
#From above code we observe that the order of the keys were not maintained i.e the sequence in which the keys were added


#Here comes the advantage of OrderedDict
#An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
from collections import*
'''d1={};print(type(d1)) #notice the difference
d=OrderedDict()
print(type(d)) #notice the difference
d["a"]=1
d["b"]=2
d["c"]=3
d["d"]=4
d["e"]=5
print(d)
for k,v in d.items():
    print("Key",k,"is associated with value",v)
'''
#will observe that it maintains the order in which the keys were added




#Equality with an Ordered Dictionary
#A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items were added.

#A Normal Dictionary


print('Dictionaries are equal?')
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'
print(d1==d2) #even though the order is not maintained
#that is the order doesn't matter in case of regular/normal dictionaries



#An Ordered Dictionary



print('Dictionaries are equal?')

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'
print(d1==d2)
#order matters very much in case of OrderedDict






