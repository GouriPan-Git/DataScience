# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:34:04 2021

@author: gouri
"""
# First function example: Add 1 to a and store as b

def Add1(a):
    x=a+1
    return (x)

b=Add1(5)
print(b)



def square(x):
    y=x*x
    return(y)

print(square(2))


# Build-in function print()

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)


# Use sum() to add every element in a list or tuple together

sum(album_ratings)

# Print the list using for loop

def PrintList(the_list):
    for element in the_list:
        print(element)
        
# Implement the printlist function

PrintList(['1', 1, 'the man', "abc"])


# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)


# Test the value with default value and with input

isGoodRating()
isGoodRating(10)



# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1) #Get Error as this variable scope is within the function and not global



artist = "Michael Jackson"
def printer1(artist):
    global glob_variable 
    glob_variable = artist
    print(artist,"is an artist")
    
printer1(artist)
print(glob_variable)


# Example of global variable and local variable with the same name

myFavoriteBand ="AC/DC"

def getBandRating(bandname):
    myFavoriteBand = "Deep Purple"
    if bandname == myFavoriteBand:
        return 10.0
    else:
        return 5.0
    
print("AC/DC rating is", getBandRating("AC/DC"))  
print("Deep Purple rating is", getBandRating("Deep Purple"))  
print("My favorite band name is ", myFavoriteBand)
    
## Collections and Functions

def printAll(*args):
    for argument in args:
        print(argument)

printAll("Rajat","Gouri","Neha","Sana")

def printDictionary(**args):
     for key in args:
         print(key + ':' + args[key])
         
printDictionary(Country = "India", State="West Bengal", PinCode="700156") 


#adding Items to list

def addItems(list):
    list.append("Three")
    list.append("Four")
    
myList = ["one","two"]
addItems(myList)

print(myList)

#Come up with a function that divides the first input by the second input:
    
def divfunc(a,b):
    x=a/b
    return(x)

print(divfunc(15,6))

# Use the con function for the following question

def con(a, b):
    return(a + b)

print(con(4,6))
print(con("one","two"))
tuple1 = (1,2,3)
tuple2 = (4,5,6)
print(con(tuple1, tuple2))
list1=["er","ei",1]
list2=[True]
print(con(list1,list2))


## Learn objects and classes

import matplotlib.pyplot as plt
%matplotlib inline

# Create a class circle

class Circle(object):
    
    #Constructor
    def __init__(self, radius=3, colour='blue'):
        self.radius = radius
        self.colour = colour
    
    #Add radius
    def add_radius(self,r):
        self.radius = self.radius + r
        return(self.radius)
    
    #Draw a circle
    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.colour))
        plt.axis('scaled')
        plt.show()  
        
RedCircle=Circle(4,'red')

print("Radius of circle", RedCircle.radius)
RedCircle.add_radius(5)
print("Radius of circle after add", RedCircle.radius)
RedCircle.draw_circle()     
dir(RedCircle)   

BlueCircle=Circle(radius=3)
BlueCircle.draw_circle()

class Rectangle(object):
    
    def __init__(self,height=4, width=5, colour='blue'):
        self.height = height
        self.width= width
        self.colour = colour
        
    def draw_Rectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.colour))
        plt.axis('scaled')
        plt.show()

blueRectangle=Rectangle(5,8,'blue')
blueRectangle.draw_Rectangle()

blueRectangle.height

# Text Analysis Tool
# ##
# You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can perform analysis on a given piece of text. Complete the class
# 'analysedText' with the following methods -

# <ul>
#     <li> Constructor - Takes argument 'text',makes it lower case and removes all punctuation. Assume only the following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?). Store the argument in "fmtText"      
#     <li> freqAll - returns a dictionary of all unique words in the text along with the number of their occurences.
#     <li> freqOf - returns the frequency of the word passed in argument.
# </ul>
#  The skeleton code has been given to you. Docstrings can be ignored for the purpose of the exercise. <br>
#  <i> Hint: Some useful functions are <code>replace()</code>, <code>lower()</code>, <code>split()</code>, <code>count()</code> </i><br>
# ##
class analysedText(object):
        fmtDict={}      
        def __init__(self,text):
            global fmtText;
            fmtText1=text.lower()
            fmtText2 = fmtText1.replace('?','')
            fmtText3 = fmtText2.replace('!','')
            fmtText4 = fmtText3.replace('.','')
            fmtText = fmtText4.replace(',','')
            #print(fmtText)
        
        def freqAll(sourceList):
            my_dict = {i:sourceList.count(i) for i in sourceList}
            return(my_dict)
        
        def freqOf(findWordFreq):
            NumofOccurences = fmtDict[findWordFreq]
            return(NumofOccurences)  
        
        
samplePassage = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
 
print(fmtText)

fmtList = fmtText.split()
print(fmtList)

fmtDict=freqAll(fmtList)
print(fmtDict)

fmtFreq = freqOf("consetetur")
print(fmtFreq)

           



    
    
#SampleList=           
