n=input("Enter name of the student:")
print(n)
c=input("Enter class of the student:")
print(c)
r=input("Enter roll no of the student:")
print(r)
m=int(input("Enter marks obtained in maths:"))
e=int(input("Enter marks obtained in english:"))
p=int(input("Enter marks obtained in physics:"))
ch=int(input("Enter marks obtained in chemistry:"))
cs=int(input("Enter marks obtained in computer science:"))
total=m+e+p+ch+cs
print("total marks of student:",total)
a=total/5
print("Percentage of students:",a)
if (a>=75):
    print("Grade of the student is distinction")
elif (a>=60 and a<75):
    print("Grade of the student is 1 division")
elif (a>=50 and a<60):
    print("Grade of the student is 2 division")
elif (a>=40 and a<50):
    print("Grade of the student is 3 division")
else:
    print("FAIL")