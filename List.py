# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 23:06:50 2018

@author: Hitesh
"""

#List in  Python.

num=[10,20,30,40,50,60,75]
print(num)
print(num[3])

print(num[0:3])

string=['Hitesh','Sannidhya','Sonal','Pratik','Nilesh']
print("Before append string is ",string)
string.append("Krunal")
print("After append string is ",string)

#Removing an item from string we use pop.
string.pop()#it will delete the last element form a string.
print(string)

#if we want ot print the perticular index of the string.
print(string[3])

#if we want to print the list in a perticular range.
print(string[1:4])

#if we want to find the length of the string.
print(len(string))# it will return total number of string in the list.

#if we want to add the another list into a list then we use append().
string.append(num)
print(string)

#extend() function use to add the item in the list.
string.extend(num)
print(string)

name=["Ganesh","Shiv","Narayan"]
print(name)

string.extend(name)
print(string)

string.extend("Hitesh")
print(string)

#If we want to delete the item from perticula range the delete() is use.
del string[8:14]
print(string)

#Insert() is use to adding the element in given position.
string.insert(3,"Ram")
print(string)

#remove() function remove the element as per given index.
string.remove('Ram')
print(string)

#sorting the string by using sort() function.
string.sort()
print(string)

#reverse the string by using reverse() function.
string.reverse()
print(string)

if "Piyush" in string:
    print("Piyush Is present in list")
else: 
    print("Piyush is not present in the list")
    
print(string.lower())

print(len(string))

print(max(string))

print(num)

print(min(num))
print(max(num))

print(sum(num))

list=string+name
print(list)

number=num*3
print(number)

print(string.count("Hitesh"))

string.insert(5,"Hitesh")

print(string)

num.insert(4,20)
print(num)
print(num.count(20))

print(num[3])

print(string[2])

print(num[1:3])

print(string[1:4])

print([num,string])
 
mix=[2.5,'Hitesh',50]

print([num,string,mix])

print(num[2:])

print(num[:3])

#Append function is use to add the item to end of list.
print(num.append(90))

print(num)

#Clear fuunction is use to remove all item to the list
print(num.clear())
print(num)

#pop function is use to delete the last element in the list.
print(num.pop())
print(num)

#Insert function is use to add the item in list as a give index.
print(num.insert(2,55))
print(num)

#Remove function is use to remove the item in the list.
print(num.remove(55))
print(num)

#Reverse function provide the reverse ordered list by given list.
print(num.reverse())
print(num)

#Sort function is use to sort th eitem in assending order.
print(num.sort())
print(num)


print(string.count())
print(num.count(10))


print(string.extend('Hitesh'))
print(string)

print(string.insert(3,'Hitesh'))
print(string)

print(string.count('Hitesh'))

print(string.reverse())
print(string)















