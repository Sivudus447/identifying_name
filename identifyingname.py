import math
a=[] 
for i in range(97,123):
    a.append(chr(i))
ss1=a[0:5]
ss2=a[5:10]
ss3=a[10:15]
ss4=a[15:20]
ss5=a[20:26]
for i in ss1:
    if(i=='a'):
        print('1.',i,end=" ")
    else:
        print(i,end=" ")
print()
for i in ss2:
    if(i=='f'):
        print('2.',i,end=" ")
    else:
        print(i,end=" ")
print()
for i in ss3:
    if(i=='k'):
        print('3.',i,end=" ")
    else:
        print(i,end=" ")
print()
for i in ss4:
    if(i=='p'):
        print('4.',i,end=" ")
    else:
        print(i,end=" ")
print()
for i in ss5:
    if(i=='u'):
        print('5.',i,end=" ")
    else:
        print(i,end=" ")
print("\n")
a=int(input('enter in your in hart ♥ name length: '))
ss=[]
for i in range(a):
    print("enter your name",(i+1),'letter ✉ row:')
    ss.append(int(input()))
print("\n")
for k in range(1,7):
    print(k,end=" ")
print()
for i in ss:
    
    if(i==1):
        for i in ss1:
            print(i,end=" ")
    if(i==2):
        for i in ss2:
            print(i,end=" ")
    if(i==3):
        for i in ss3:
            print(i,end=" ")
    
    if(i==4):
        for i in ss4:
            print(i,end=" ")
    if(i==5):
        for i in ss5:                   #row elements ss colum s
            print(i,end=" ")
    print("")
s=[]
for i in range(a):
    print("enter your name",i+1,"letter ✉ column: ")
    b=int(input())
    s.append(b)
m=[]
for i in (ss):
    if(i==1):
        m.append(ss1)
    elif(i==2):
        m.append(ss2)
    elif(i==3):
        m.append(ss3)
    elif(i==4):
        m.append(ss4)
    else:
        m.append(ss5)
a=[]
b=[]
c=[]
q=0
for j in m:
    r=(s[q]-1)
    a.append(j)
    for i in a:
        for t in i:
            b.append(t)
        c.append(b[r])
        b.clear()
    a.clear()
    q+=1 
print("in your thinking name is 😱:")
for l in c:
    print(l,end="")
