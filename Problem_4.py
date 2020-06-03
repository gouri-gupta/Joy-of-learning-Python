print("Problem statement 4:")
print('''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 
9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.''')

def fun(n):
    a=10**(n-1)
    b=10**n
    l = []
    for i in range(a,b):
        for j in range(a,b):
            c = i * j
            p=str(c)
            k = p[::-1]
            if (p == k):
                l.append(c)
            else:
                pass
    print(l)
    print(max(l),"is the largest palindrome made from the product of two 3-digit numbers")
n=int(input("Enter how many digits you want to include so as to get the largest pallindrome made from the product of n-digit numbers: "))
fun(n)