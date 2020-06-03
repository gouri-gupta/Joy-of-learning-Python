#Level 2 problems
'''FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''

'''def has_33(l):
    for i in range(0,len(l)):
        if (i!=len(l)-1):
            if (l[i]==l[i+1]):
                if (l[i]==3):
                    return True
    else:
        return False
n=int(input("Enter the length of list:"))
l=[]
for i in range(0,n):
    a=int(input(("Enter the {} element of the list:".format(i+1))))
    l.append(a)
print(has_33(l))
'''


'''
def has_33(nums):
    for i in range(0, len(nums)-1):
      
        # nicer looking alternative in commented code
        #if nums[i] == 3 and nums[i+1] == 3:
    
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False
'''






'''PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''

'''def paper_doll(s):
    a=""
    for i in range(0,len(s)):
        a+=(s[i]*3)
    return a
s=input("Enter any string:")
print(paper_doll(s))
'''


'''
def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result
'''







'''BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) 
exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''

'''def blackjack(l):
    s=sum(l)
    if (s<=21):
        return s
    else:
        for i in l:
            if (i==11):
                return s-10
        else:
            return "BUST"
l=[]
print("Enter a number between 1 to 11 including 1 and 11")
for i in range(3):
    n=int(input("Enter the {} element:".format(i+1)))
    if (n>=1 and n<=11):
        l.append(n)
print(blackjack(l))'''



'''
def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <=31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
'''





'''SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
'''
'''def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
print(summer_69([2,1,6,9,11]))
'''






'''
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
'''
'''
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works
    return len(code) == 1
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
'''




'''COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25
'''

'''def count_primes(n):
    l=[]
    for i in range (2,n+1):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            l.append(i)
    return len(l)
n=int(input("Enter the number up to which you want ot know how many prime numbers exist:"))
print(count_primes(n))
'''





'''PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *
HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
For purposes of this exercise, it's ok if your dictionary stops at "E".
'''
'''
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print(print_big('e'))
'''