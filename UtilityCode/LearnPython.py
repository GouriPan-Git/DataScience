# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:31:49 2021

@author: gouri
"""

# This is used to write comments

# Try to print Hello

print("Hello! Python")

# To know the version of python being used

import sys
print(sys.version)

# Print string and error to see the running order

print("This will be printed")
#frint("This will cause an error")
print("This will NOT be printed")


# print "Hello, World!"

print("Hello, World!") #Print the traditional Hello World

# Integer

type(10)

# Float

type(4.5)

# String

type("Hello")


sys.float_info


# Converting Integers to float

type(float(10))

type(float(5.5))

type(int(6.5))

#Converting string to int or float
type(int('1.2')) #Error invalid literal for int()

type(int('1'))

type(float('1.2'))

type(float('1 0r 2')) #Error could not convert string to float

# Converting interger or float to string

type(str(1))  # output str

str(1) # output '1'

str(1.1) # output '1.1'

#Boolean

type(True)  # bool

type(False)  #bool

bool(1)   # True

bool(0)  # False

float(True)  #1.0

float(False)  #0.0

# Division

6/2  #3.0

6//2 # 3 integer output


#How many hours are there in 160 minutes

160//60  # 2 hours

# String Operations

Name = "Michael Jackson"
print(Name[-1])
print(Name[0])

print(Name[0:4])
print(Name[8:12])
print(Name[::2])
print(Name[0:5:2])

statement = Name + "is the best"

print(3*Name)

# New line escape sequence

print(" Michael Jackson \n is the best" )

# Tab escape sequence

print(" Michael Jackson \t is the best" )


# Include back slash in string

print(" Michael Jackson \\ is the best" )

# r will tell python that string will be display as raw string

print(r" Michael Jackson \ is the best" )

# String Method 

a = "This string will be moved to upper"
print("before upper method :" + a)
b=a.upper()
print("after the upper method :" + b)

b=a.replace("moved to","replaced by")
print(b)


a.find("fore")
a.find("move")
b.find("repl")   #Find is case sensitive

a = "1"
print(a)

b = "2"
print(b)

print(a+b)

#Use a stride value of 2 to print out every second character of the string e
e = 'clocrkr1e1c1t'
print(e[::2])

r="This is the \\ backslash print"
print(r)


# Write your code below and convert to upper

f = "You are wrong"

print(f.upper())


# Write your code below Consider the variable g, and find the first index of the sub-string snow:

g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

g.find("snow")

# In the variable g, replace the sub-string Mary with Bob:

g.replace("Mary", "Bob")



