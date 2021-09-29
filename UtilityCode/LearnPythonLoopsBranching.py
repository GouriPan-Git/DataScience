# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:53:27 2021

@author: gouri
"""
#Conditions and Branching
# Write an if statement to determine if an album had a rating greater than 8. 
#Test it using the rating for the album “Back in Black” that had a rating of 8.5. 
#If the statement is true print "This album is Amazing!"

album_rating=8.5

if album_rating>8:
    print("This album is Amazing")
    
#Write an if-else statement that performs the following. 
#If the rating is larger then eight print “this album is amazing”. 
#If the rating is less than or equal to 8 print “this album is ok”.

album_rating=8

if album_rating>8:
    print("This album is Amazing")
else:
    print("This album is Ok")
    
    
# Write an if statement to determine if an album came out before 1980 
# or in the years: 1991 or 1993. If the condition is true 
# print out the year the album came out.

album_release_year = 1991

if(album_release_year<1980) or (album_release_year==1991) or (album_release_year==1993):
   print("The album was released in the year ", album_release_year)
   
#Loops For and while

# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])     
    
    
# Example of for loop

for i in range(0, 8):
    print(i)
    
    
dates = [1982,1980,1973] 
for year in dates:
    print(year)