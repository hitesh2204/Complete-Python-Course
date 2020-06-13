# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:17:57 2019

@author: Hitesh
"""

"""LIST."""
#checking item present in list or not.
Name=['Hitesh','Krunal','Saku','Sannu','Pritam','Hitesh']
print(Name)

Age=[27,29,30,21,30,34]
print(Age)

"""Condition to check if element is in List."""
element in Name

if 'Hitesh' in Name:
    print(" Hitesh is present in ",Name)
    
if 'Yerekar' not in Name:
    print("Yerekar not present in ",Name)
    
if Name.count('Hitesh')>0:
    print("Hitesh found in Name",Name)    
    
result=all(elem in Name for elem in Age) 
print(result)
if result:
    print("Name contains elements from Age")
else:
    print("Name not contains elements from Age")
    
result1=any(elem in Name for elem in Age)
print(result) 
if result:
    print("Name contains elements from Age")
else:
    print("Name not contains elements from Age")   

List=["Hi" for i in range(20)]
print(List)

List=["Hello"]*10
print(List)

"""For Loop."""
for i in Name:
    print(i)
    
"""While Loop."""
i=0
size=len(Name)
while i<size:
    if i%2==1:
        print(size[i])
    i+=1
    
    
for i in range(len(Name)):
    print(Name[i])
    i+=1    
    
Name.insert(3,"Rucha")
print(Name)    
    
Name.sort()

Name.sort(reverse=True)
print(Name)

num=[20,15,40,60,32,29,77,81,10]
print(num)
    
num.sort(key=int)
print(num)  

num.sort(reverse=True,key=int)
print(num)  
    
Name.append("Piyush")
print(Name)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    