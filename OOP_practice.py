'''Write a class Cylinder that computes the volume and surface area of the cylinder'''
'''
class Cylinder:
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    def surface_area(self):
        return 2*3.14*self.radius*(self.height+self.radius)
    def volume(self):
        return 3.14*(self.radius**2)*self.height
r=int(input("Enter the radius of the Cylinder:"))
h=int(input("Enter the height of the Cylinder:"))
c=Cylinder(r,h)
print("The Surface area of the cylinder is",c.surface_area())
print("The volume of the cylinder is",c.volume())
'''





'''Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.'''
'''
class Line:
    def __init__(self,t1,t2):
        self.y2=t2[1]
        self.y1=t1[1]
        self.x2=t2[0]
        self.x1=t1[0]
    def slope(self):
        return ((self.y2-self.y1)/(self.x2-self.x1))
    def distance(self):
        a=((self.x2-self.x1)**2)+((self.y2-self.y1)**2)
        return a**0.5
t1=[]
t2=[]
l=int(input("Enter the x co-ordinate of the point t1:"))
m=int(input("Enter the y co-ordinate of the point t2:"))
t1.extend([l,m])
x=int(input("Enter the x co-ordinate of the point t1:"))
y=int(input("Enter the y co-ordinate of the point t2:"))
t2.extend([x,y])
a=tuple(t1);b=tuple(t2)
print("The two points are",a,"and",b)
s=Line(a,b)
print("The slope of the line is:",s.slope())
print("The distance between the two points is:",s.distance())
'''