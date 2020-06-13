# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 02:15:34 2018

@author: Hitesh
"""

# Assigning the value to variable.
welcome="Hello Hitesh"
print(welcome)

#Assigning the multiple value to the variables.
a,b,c=10,50.5,"Hitesh"
print(a)
print(b)
print(c)

x=y=z="Hello Hitesh"
print(x)
print(y)
print(z)

#Constant 
PI=3.14
print(PI)
GRAVITY=9.8
print(GRAVITY)

import constant
print(constant.PI)
print(constant.GRAVITY)


#Literals in Python.
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

#String Literals.
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

#Boolean Literals
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

#Literals Collection in python.
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

#Converting Integer to float.
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

#Converting string to integer
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

print(num_int+num_str)

#Type Casting.

num_int=123
num_str="567"
print(type(num_int))
print(type(num_str))

#converting the string into integer
num_str=int(num_str)
print(type(num_str))

#addintion of this integer.
num_new=num_int+num_str
print(num_new)


#Convertinh the integer to float.
a=10
print(a)

k=float(a)
print(k)

#Converting float to integer.
x=10.50
k=int(x)
print(k)

#complex number.
k=5+6j
print(k)
type(k)

c=x>a
print(c)

#Dictionary..........
d={'Hitesh':'Mi','Rahul':'Iphone','Kunal':'Nokia','Pratik':'Samsung','Sonal':'OnePlus'}
print(d)

d('Hitesh')

d.keys()

d.values()

d['Hitesh']
d['Kunal']

d.get('Hitesh')
d.get('Sonal')

#Changing the values in the dictionary.
d['Hitesh']='MI_Note 4'
print(d)

#Adding the item in the dictionary.
d['Rucha']='Oppo'
print(d)

#Finding the length of dictionary.
print(len(d))

#Removing the item in dictionary by using the key.
del d['Kunal']
print(d)

#dict Constructor for crating the dictionary.
x=dict(name="Hitesh",age=27,profession="Software Engineer",city="Pune")
print(x)

x['name']
x['age']
x['profession']
x['city']

#Copying the dictionary.
z=x.copy()
print(z)

c=d.copy()
print(c)

#Fromkeys use in dictionary.
x={'name','rollno','age'}


z=dict.fromkeys(x)
print(z)

#Item() function used to pair the key and value of dictionary.
z=x.items()
print(z)

q=x.setdefault('Lname','Yerekar')
print(q)


#accessing the data by using the indexes.
import pandas as pd
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s[0])

print(s[:3])

#creating the empty dataframe.
import pandas as pd
df=pd.DataFrame()
print(df)


#creating dataframe from list.
import pandas as pd
data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)

data=[["hitesh",27],["Sonal",30],["Sannu",1]]
df=pd.DataFrame(data,columns=["Name","Age"])
print(df)

data=[['hitesh',27],['sohen',30],['pratik',26]]
df=pd.DataFrame(data,columns=('Name','Age'),dtype=float)
print(df)

#Creating the dataframe from ndarray/list.

data={'Name':['Hitesh','Soanl','Sannidhya'],'Age':[27,30,1]}
df=pd.DataFrame(data)
print(df)

data={'Name':['Hitesh','Soanl','Sannidhya'],'Age':[27,30,1]}
df=pd.DataFrame(data,index=[100,200,300])
print(df)

data=[{'a':1,'b':2},{'a':3,'b':4,'c':5}]
df=pd.DataFrame(data)
print(df)

data=[{'a':1,'b':2},{'a':3,'b':4,'c':5}]
df=pd.DataFrame(data,index=['first','second'])
print(df)

a=16
b=5
c=a//b    #It gives the quotients.
print(c)

d=a%b     #Its gives you remainder.
print(d)

e=20/b
print(e)

dir()

a=3
b=5

a==b

a!=b

a>b

a<b

import datetime
now=datetime.datetime.today()
print(now)


name=input("Eneter your name")
print(name)

dir(set)





