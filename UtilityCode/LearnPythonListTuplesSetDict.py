# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:11:41 2021

@author: gouri
"""

# Create a List

L = ["Michael Jackson", 10.1, 1]
L

L[1]

print ('Element of list using positive index', L[0], '\n Element of List using negative index ' , L[-1])

L.extend(['MJ', 1982])

L

L[3:5]

L.append(['pop',9])

del(L)
#List is mutable
A = ["Disco",10,8.9]
print("Before Change", A)
A[0] = "Hard Rock"
print("After Change", A)

"Hard Rock".split()

"A,B,C,D".split(',')
#Both refer to the same location Copy by Reference
B=A

print("list A is", A)
print("list B is", B)

A[0]="Banana"

print("list A is", A)
print("list B is", B)

#Cloning Clone by Value

B=A[:]

A[0]="Hard Rock"

a_list=[1, 'hello', [1,2,3], True]
a_list

a_list[1:4]

del(A)
del(B)

A=[1,'a']
B=[2,1,'d']

A+B

# Dictionary

Dict = {"Key1": 1, "Key2" : "2", "Key 3":[3,3,3], "Key4":(4,4,4), ('key5'):5}

Dict["Key1"]

Dict[(0, 1)] # Error

# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict

# Get value by keys

release_year_dict['Thriller'] 

# Get all the keys in dictionary

release_year_dict.keys()

# Get all the values in dictionary

release_year_dict.values()

# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict


# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict

# Question sample dictionary

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 

soundtrack_dic.keys()
soundtrack_dic.values()



album_sales_dict ={"The Albums Back in Black" : 50, "The Bodyguard" : 50, "Thriller" : 65}
album_sales_dict

Total_sales_Of_Thriller = album_sales_dict["Thriller"]
Total_sales_Of_Thriller

album_sales_dict.keys()
album_sales_dict.values()

# Create your first tuple

tuple1 = ("disco",10,1.2 )
tuple1

# Print the type of the tuple you created

type(tuple1)

tuple1[0]
tuple1[-3]

# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
tuple2

tuple2[0:3]
tuple2[3:5]

len(tuple2)


Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
# Sort the tuple

RatingsSorted = sorted(Ratings)
RatingsSorted

# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])


genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple

len(genres_tuple)

genres_tuple[3]

genres_tuple[3:6]

genres_tuple[0:2]

genres_tuple.index("disco")
C_tuple=(-5, 1, -3)

C_tuple_sorted = sorted(C_tuple)
C_tuple_sorted

# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1


# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set

# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres

# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
A

A.add("NSYNC")
A

A.remove("NSYNC")
A

# Verify if the element is in the set

"AC/DC" in A

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])


# Print two sets

album_set1, album_set2


# Find the intersections

intersection = album_set1 & album_set2
intersection


album_set1.difference(album_set2)  #{'Thriller'}

album_set2.difference(album_set1) #{'The Dark Side of the Moon'}

album_set1.intersection(album_set2)   


# Find the union of two sets

album_set1.union(album_set2)


# Check if superset

set(album_set1).issuperset(album_set2)   

# Check if subset

set(album_set2).issubset(album_set1)     

music_genres = set(['rap','house','electronic music', 'rap'])
type(music_genres)

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])

B
A

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_set3 = album_set1.union(album_set2)
album_set3

album_set1.issubset(album_set3)