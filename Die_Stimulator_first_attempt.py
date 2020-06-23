#A symbolic representation of a DIE
'''
p={"a":"    *    ","b":"*","c":"        *"}
r={1:p["a"],2:p["b"]+p["c"],3:p["b"]+"\n"+p["a"]+"\n"+p["c"],4:p["b"]+p["c"]+"\n"+p["b"]+p["c"],5:p["b"]+p["c"]+"\n"+p["a"]+"\n"+p["b"]+p["c"],6:(p["b"]+p["a"]+p["b"]+"\n")*2}
#for i in range(1,7):
 #   print(r[i]+"\n")
from random import*
a=randint(1,6)


print("[--------]")
print("[        ]")
print("["+r[a]+"]")
print("[        ]")
print("[--------]")
'''





#Another graphical explanation for a DIE


a="|"
p={1:a,2:(a*2),3:(a*3),4:(a*4),5:(a*5),6:(a*6)}
from random import*
s=randint(1,6)
#print(p[s].center(8))
d="It's a"
print("Type 1:")
print("[--------]")
print("["+d.center(8)+"]")
print("["+p[s].center(8)+"]")
print("["+str(s).center(8)+"]")
print("[--------]")

print("\nType 2:")
print(" ________")
print("[        ]")
print("|"+d.center(8)+"|")
print("|"+p[s].center(8)+"|")
print("|"+str(s).center(8)+"|")
print("[________]")

print("\nType 3:")
print("/"*10)
print("\\"+d.center(8)+"\\")
print("/"+p[s].center(8)+"/")
print("\\"+str(s).center(8)+"\\")
print("/"*10)


print("\nType 4:")
print("/"*10)
print("/"+d.center(8)+"/")
print("/"+p[s].center(8)+"/")
print("/"+str(s).center(8)+"/")
print("/"*10)

print("\nType 5:")
print("||||||||||")
print("|"+d.center(8)+"|")
print("|"+p[s].center(8)+"|")
print("|"+str(s).center(8)+"|")
print("||||||||||")

f={1:"i",2:"ii",3:"iii",4:"iv",5:"v",6:"vi"}

print("\nType 6(Some fun with small roman letters):")
print("||||||||||")
print("|"+d.center(8)+"|")
print("|"+f[s].center(8)+"|")
print("|"+str(s).center(8)+"|")
print("||||||||||")


e={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI"}
print("\nType 7(Some fun with Capital Roman letters):")
print("||||||||||")
print("|"+d.center(8)+"|")
print("|"+e[s].center(8)+"|")
print("|"+str(s).center(8)+"|")
print("||||||||||")

print("\nType 8:")
print("[--------]")
print("["+d.center(8)+"]")
print("["+e[s].center(8)+"]")
print("["+str(s).center(8)+"]")
print("[--------]")

print("\nType 9:")
print("/"*10)
print("/"+d.center(8)+"/")
print("/"+f[s].center(8)+"/")
print("/"+str(s).center(8)+"/")
print("/"*10)

