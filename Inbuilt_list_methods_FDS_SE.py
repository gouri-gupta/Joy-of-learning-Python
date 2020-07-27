def maximum_element(l):
    '''This function calculates the maximum element from the list'''
    a=l[0]
    for i in range(1,len(l)):
        if (a<l[i]):
            a=l[i]
        else:
            pass
    print("Maximum element of the list is:",a)
#maximum_element([1,2,3,4,5,5])

def minimum_element(l):
    '''This function calculates the maximum element from the list'''
    a=l[0]
    for i in range(1,len(l)):
        if (a>l[i]):
            a=l[i]
        else:
            pass
    print("Minimum element of the list is:",a)
#minimum_element([64,5587,4553,5486,65,598])

def to_calculate_length_of_list(l):
    length=0
    for i in l:
        length+=1
    return length
z=to_calculate_length_of_list([1,2,3,54,5,6])
#print("The length of list [1,2,3,54,5,6] is",z)
l=[1,2,3]


def to_append_element_in_list(l,n):
    x=to_calculate_length_of_list(l)
    l+=[n]
    #print(l)
    return l
l=[1,2,3]
to_append_element_in_list(l,4)
to_append_element_in_list(l,5)
to_append_element_in_list(l,88)
to_append_element_in_list([1,2,4,55,5,55,8],9)

def to_calculate_intersection_between_two_sets(a,b):
    '''This function calculates the intersection of sequences a and b'''
    a_intersect_b=[]
    for i in a:
        if i in b:
            intersection_set=to_append_element_in_list(a_intersect_b,i)
    return intersection_set
to_calculate_intersection_between_two_sets([1,2,3,4,5,6],[3,4,5,6])


def to_calculate_union(a,b):
    union=[]
    for i in a:
        union_fu=to_append_element_in_list(union,i)
    for i in b:
        if i in union:
            pass
        else:
            union_f1=to_append_element_in_list(union,i)
    return union
#print(to_calculate_union([1,2,3],[3,4,5]))


def to_calculate_symmetric_difference(a,b):
    intersect_bet_a_b=to_calculate_intersection_between_two_sets(a,b)
    union_of_a_b=to_calculate_union(a,b)
    symmetric_diff_list=[]
    for i in union_of_a_b:
        if i in intersect_bet_a_b:
            pass
        else:
            k1=to_append_element_in_list(symmetric_diff_list,i)
    return symmetric_diff_list
#print(to_calculate_symmetric_difference([1,2,3],[3,4,5]))
#print("🏏\U0001F3CF🏏🏏")
#print("\U0001F3F8")
#print("\U000026BD")