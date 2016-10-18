print("this is app1 version 0.1")
print("this will switch to version 0.2")

#ex1
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j and j!=k and i!=k):
                print(i,j,k)
'''

#ex2
'''
import math
for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if(x*x==i+100 and y*y==i+268):
        print("result: %d"%i)
        break
'''

#ex3
'''
li=[]
for i in range(3):
    x=int(input("input integer:"))
    li.append(x)
li.sort()
print(li)
'''

#ex4
'''
i=input("input number:")
number=int(i)
li=[]
for it in range(0,number+1):
    li.append(True)
    
li[0]=False
li[1]=False
li[2]=False
for i in range(2,number+1):
    j=i
    mult=2
    while j<number+1:
        j=i*mult
        mult+=1
        if j<number+1:
            li[j]=False
for i in range(1,number+1):
    if li[i]==True:
        print(i)
'''

#ex5
'''
i=input("input number:")
number=int(i)
for n in range(1,number):
    tmp=n
    li=[]
    while tmp!=0:
        tmp2=tmp%10
        li.append(tmp2)
        tmp=tmp//10
    count=0
    for elem in li:
        count+=elem**3
    if count==n:
        print(n)
'''


    
    
    
