f=open("assignment8.txt","r")
l=0
w=0
c=0
sw=input("Enter the word to be searched:")
count=0
#l1=[]
for line in f:
    l+=1
    for word in line.split():
        w+=1
        #l1.append(w)
        for j in word:
            c+=1
for lineno,lines in enumerate(f,1):
    count+=lines.count(sw)
'''t=0
for i in l1:
    if i==sw:
        t+=1'''
print("There are total",l,"lines present in the file")
print("There are total",w,"words present in the file")
print("There are total",c,"characters present in the file")
print("The entered word",sw,"has occured",count,"times in the file")