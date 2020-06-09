'''Counter is a dict subclass which helps count hashable objects. Inside of it elements are stored as dictionary keys
and the counts of the objects are stored as the value.'''
from collections import*
l=[1,2,2,3,44,4,5,5,1,1,2,2,1,2,5,8,12,16,3,4,6,9]
print(Counter(l))
'''The above statement will return a dictionary in which the keys will be the elements stored in the list and their values will be the number of times that
associated key (i.e the element) is present in the list or the sequence as shown in the above example'''
s="ssssaaaaaaaaakkiiiyrrrrrrrrrjjdvbejdgndkgkhksjdmmmmmmm"
print(Counter(s))
a="How many times each word has appeared in the given sentence?"
print(Counter(a)) #will count each character present in the a
#However,if we want to count the how many times a particular word has appeared in the given sentence i.e a
l1=a.split()
print(l1)
print(Counter(l1))
a+=" How many times?"
print(Counter(a))
l2=a.split()
print(Counter(l2))
c=Counter(l2)
print(type(c))
print(c.most_common(3)) #most common three words
print(c.most_common(2)) #most common two words




#Extra functions which can be performed with the Counter function
#Common patterns when using the Counter() object
#sum(c.values())                  total of all counts
#c.clear()                        reset all counts
#list(c)                          list unique elements
#set(c)                           convert to a set
#dict(c)                         convert to a regular dictionary
#c.items()                        convert to a list of (elem, cnt) pairs
#Counter(dict(list_of_pairs))     convert from a list of (elem, cnt) pairs
#c.most_common()[:-n-1:-1]       n least common elements
#c += Counter()                   remove zero and negative counts

print(sum(c.values())) #total of all counts


'''
print(c.clear()) #will clear all the elements of the dictionary i.e reset all counts
print(c)
print(c.most_common(3)) #will return an empty list 
'''


print(list(c)) #list unique elements
print(tuple(c)) #convert into a tuple
print(set(c))  #convert into a set
print(dict(c)) #will print the same dictionary but without the counter word i.e convert to a regular dictionary


print(c.items())  #convert to a list of (elem, count) pairs



