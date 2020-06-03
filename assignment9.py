'''class ABC:
    var=10
    def display(self,s):
        self.s=s
        print("1",self.s)
        print("2",s)
        print("Inside class ABC's method")
obj=ABC()
s=input("Enter any value:")
obj.display(s)
a=ABC()
a.display(5)
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("The entered arguments are:",self.a,self.b)
a=input("Enter 1st argument:")
b=input("Enter 2nd argument:")
c=A(a,b)
class A:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def display(self):
        print("The entered arguments are:",self.cpu,self.ram)
a=input("Enter cpu")
b=input("Enter ram")
c=A(a,b)
c.display()
class Employee:
    def __init__(self,n):
        self.n=n
    def display(self):
        for i in range(self.n):
            g = input("Enter m for male\nEnter f for female\nEnter your gender:")
            name = input("Enter your name:")
            p = input("Enter your designation:")
            s = int(input("Enter your salary:"))
            d = input("Enter your joining date in the organization:")
            if (g=='m'):
                print("Hello Mr."+name)
            elif (g=='f'):
                print("Hello Miss/Mrs."+name)
            else:
                print("Enter a valid gender")
            print("Your desination in the organization is",p)
            print("You joined the organization on",d)
            if (s>10000):
                print("Your salary is greater than 10000")
            else:
                print("Your salary is not greater than 10000")
n=int(input("Enter number of employees present in the organization:"))
c=Employee(n)
c.display()'''
class Employee:
    Employee_count=0
    males=0
    females=0
    def __init__(self,name,gender,designation,jdate,salary):
        self.name=name
        self.gender=gender
        self.jdate=jdate
        self.salary=salary
        self.designation=designation
    def names(self):
        return self.name
    def jdate(self):
        return self.jdate
    def gen(self):
        if (self.gender=='m'or self.gender=='M'):
            Employee.males+=1
            Employee.Employee_count+=1
        elif (self.gender=='f'or self.gender=='F'):
            Employee.females+=1
            Employee.Employee_count+=1
    def design(self):
        if (self.designation=='ASSISTANT MANAGER' or self.designation=='assistant manager' or self.designation=='AM'):
            return True
        else:
            return False
    def sal(self):
        if self.salary>10000:
            return True
        else:
            return False

def create(i):
    if (i=='y'or i=='Y'):
        n=input("Enter name of Employee:")
        g=input("Enter gender of Employee:")
        j=input("Enter the joining date of Employee:")
        s=int(input("Enter the salary of Employee:"))
        d=input("Enter the designation of Employee:")
        emp=Employee(n,g,d,j,s)
        print("1.Employee name\n2.Joining Date\n3.Gender\n4.Designation\n5.Salary")
        c=int(input("Enter your choice:"))
        if c==1:
            print("Name of the Employee is",emp.names())
        elif c==2:
            print("The Employee joined the company on",emp.jdate())
        elif c==3:
            emp.gen()
            print("There are total", Employee.Employee_count, "employees present in your company")
            print("There are", Employee.males, "males in your company")
            print("There are", Employee.females, "females in your company")

        elif c==4:
            if emp.design():
                print("The Employee is an assistant Manager")
            else:
                print("Your Employee is working in the company and is not in the post of assistant manager")
        elif c==5:

            if emp.sal():
                print("The entered employee is having salary above 10,000")
            else:
                print("The entered employee is not having salary above 10,000")
        else:
            print("Your desired operation cannot be executed")
    j = input("Do you want to continue writing the other employee names\nEnter 'y' or 'Y' for yes:")
    if (j=='y' or j=='Y'):
        create(j)

i=input("Do you want to write the employee name\nEnter 'y' or 'Y' for yes:")
create(i)