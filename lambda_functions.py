#Map function
'''def square(num):
    return num**2
my_nums = [1,2,3,4,5]
print(map(square,my_nums))
#<map at 0x205baec21d0> will return the address at which the answer of the map function will be stored
# To get the results, either iterate through map()
# or just cast to a list
print (list(map(square,my_nums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
mynames = ['John','Cindy','Sarah','Kelly','Mike']
print(list(map(splicer,mynames)))'''






#Filter function
'''def check_even(num):
    return num % 2 == 0
nums = [0,1,2,3,4,5,6,7,8,9,10]
print(filter(check_even,nums))#will return the address at which the result of the filter function is stored
print(list(filter(check_even,nums)))
'''




#Lambda function
'''
square=lambda n:n**2
print(square(2))
print((lambda n:n**3)(3))
print((lambda n:n%2==0)(n=int(input("Enter any number:"))))
'''
#Basic syntax of writting lambda functions:
# lambda arguments:operation_to_be_performed or body_of_lambda_functions





#Use of Lambda functions in map and filter furnction
'''
my_nums=[12,3,4,56,7,8,94]
nums=my_nums
print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda n: n % 2 == 0,nums)))
'''





#Reduce function is also available in python
'''
l1=[1,2,3]
l2=[1,2,3]
l3=[1,2,3]
print(list(map(lambda a,b:a+b,l1,l2)))
print(list(map(lambda a,b,c:a+b+c,l1,l2,l3)))


from functools import*
print(reduce(lambda a,b:a+b,l1))
print(reduce(lambda a,b:a-b,l1))
print(reduce(lambda a,b:(a**2)+b,l1))
print(reduce(lambda a,b:a+b,list(map(lambda a,b:a+b,l1,l2 ))))
print(reduce(lambda a,b:a+b,list(map(lambda a,b,c:a+b+c,l1,l2,l3 ))))
'''