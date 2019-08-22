# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:47:02 2019

@author: rpava
"""

key=input("Enter the key= ")
key=key.lower()
print(key)
keymatrix=[]
n=len(key)
if n==4:
    n=2
elif n==9:
    n=3
for i in range(n):
    keymatrix.append([])
l=0
k=0
for i in key:
    keymatrix[k].append(i)
    if l==n-1:
        l=0
        k=k+1
    else:
        l=l+1

for i in range(len(keymatrix)):
    for j in range(len(keymatrix[i])):
        keymatrix[i][j]=ord(keymatrix[i][j])-97

data=0

data=keymatrix[0][0]*keymatrix[1][1]-keymatrix[0][1]*keymatrix[1][0]
while data<0:
   data=data+26

def gcd(a,b):  
    if (b==0): 
         return a 
    return gcd(b,a%b)
if gcd(data,26)==1:
    pt=input("Enter the text you want to encrypt= ")
    pt=pt.lower()
    plaintext=""
    for i in pt:
        if i!=" ":
            plaintext=plaintext+i
    pt=plaintext
    my_list=[]
    for i in pt:
        my_list.append(i)
    final=[my_list[i*n:(i + 1)*n] for i in range((len(my_list)+n-1)//n)]  

    for i in final:
        if (len(i)==1 and n==2):
            i.append("x")
        elif len(i)==2 and n==3:
            i.append("x")
        elif len(i)==1 and n==3:
            i.append("x")
            i.append("x")

    for i in range(len(final)):
        for j in range(len(final[i])):
            final[i][j]=ord(final[i][j])-97


    def mm(m1,m2):
        resu=[]
        for i in range(len(m1)):
            resu.append([])
            for j in range(len(m2[0])):
                resu[i].append(0)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    resu[i][j]+= m1[i][k]*m2[k][j]
        return resu
    el=[]
    result=[]
    for i in final:
        for j in i:
            el.append([j])
        ki=mm(keymatrix,el)
        result.append(ki)
        el=[]

    res=""
    for i in result:
        for j in i:
            for kee in j:
                res+=str(kee)+" "
 
    res=res.split()
    u=[]
    for i in res:
        i=int(i)
        i=i%26
        i=i+97
        i=chr(i)
        u.append(i)

    u="".join(u)
    print(u.upper())
    
    decryp=input("Enter the text to decrypt= ")
    decryp=decryp.lower()
    plaintext=""
    for i in decryp:
        if i!=" ":
            plaintext=plaintext+i
    decryp=plaintext
    my_list=[]
    for i in decryp:
        my_list.append(i)
    final=[my_list[i*n:(i + 1)*n] for i in range((len(my_list)+n-1)//n)]  

    for i in final:
        if len(i)==1 and n==2:
            i.append("x")
        elif len(i)==2 and n==3:
            i.append("x")
        elif len(i)==1 and n==3:
            i.append("x")
            i.append("x")

    for i in range(len(final)):
        for j in range(len(final[i])):
            final[i][j]=ord(final[i][j])-97
    count=1
    det=data
    while 1:
        if data%26==1:
            break
        data=data+det
        count+=1
    

decm=[[keymatrix[1][1],-keymatrix[0][1]],[-keymatrix[1][0],keymatrix[0][0]]]
for i in range(2):
    for j in range(2):
        while decm[i][j]<0:
            decm[i][j]+=26
for i in range(2):
    for j in range(2):
        decm[i][j]=count*decm[i][j]

    el=[]
    result=[]
    for i in final:
        for j in i:
            el.append([j])
        ki=mm(decm,el)
        result.append(ki)
        el=[]
    res=""
    for i in result:
        for j in i:
            for kee in j:
                res+=str(kee)+" "
    res=res.split()
    u=[]
    for i in res:
        i=int(i)
        i=i%26
        i=i+97
        i=chr(i)
        u.append(i)
    u="".join(u)
    print(u.upper())

else:
    print("Impossible!")