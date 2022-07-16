#!/usr/bin/env python
# coding: utf-8

# # 1_1_2_Data_Structures.ipynb

# # Data Structures
# 
# ### data structure
# An organization of data for the purpose of making it easier to use.
# ### immutable data value
# A data value which cannot be modified. Assignments to elements or slices (sub-parts) of immutable values cause a runtime error.
# ### mutable data value
# A data value which can be modified. The types of all mutable values are compound types. Lists and dictionaries are mutable; strings and tuples are not.
# 
# 
# ### Following are the primary Data Structures that we will study:
# **1. Strings**
# Collection of unicode characters. It is indexed and immutable, "hello world!"
# 
# **2. Lists**
# Collection of elements. It is indexed and mutable. Allows duplicates, \[10,20,30\]
# 
# **3. Tuple**
# Collection which can be indexed but immutable, (apple, 250)
# 
# **4. Set**
# Collection of unordered elements that doesn't allow repetitions, {apple, orange}
# 
# **5. Dictionary**
# Collection of Key-Value pairs, {key:value}

# # List
# A single list can have DataTypes such as Integers, Strings, as well as Objects. Lists are mutable and may therefore be modified even after they have been created. List in Python are ordered and have a definite count. The items in a list are indexed according to a defined sequence and the indexing of a list is performed with 0 being the first index. Each element of the list has its place in the list, which makes it possible to duplicate the elements of the list, with each element having its own distinct place and credibility.
# 
# Lists can be created by just placing the sequence inside the square brackets[].
# Lets learn how to create a list and see how it works.
# 

# In[1]:


List = []
print(List)


# In[2]:


#States in Nigeria
Nigeria = ['Imo', 'Abia', 'Anambra', 'Lagos', 'Uyo', 'Rivers', 'Ogun', 'Oyo', 'Osun', 'Kaduna']


# In[3]:


print(Nigeria)


# In[4]:


#List can have duplicates with each element having its own distinct place.
Revenue = [20, 30, 40, 50, 60, 70, 80, 100, 55, 60]
print(Revenue)


# ## List Operations

# In[5]:


Nigeria.append('Kastina') #Apend: Add an element to the end of the list


# In[6]:


print(Nigeria)


# In[7]:


Nigeria.insert(3, 'Kano') # Insert : Insert an item at the defined index to the list


# In[8]:


print(Nigeria)


# In[9]:


Nigeria.remove('Kano') # Remove: Removes an item from the list


# In[10]:


print(Nigeria)


# In[11]:


Nigeria.sort() #Sort items in a list in ascending order
print(Nigeria)


# In[12]:


Nigeria.reverse() #Reverse: Reverse the order of items in the list
print(Nigeria)


# In[13]:


Nigeria.insert(3, 'Kano')
print(Nigeria)


# In[14]:


Nigeria.pop(3) #Removes and returns an element at the given index
print(Nigeria)


# In[15]:


Nigeria[1:5] # items in a list that starts with 1 and ends in 4


# In[16]:


Nigeria[4:10]


# In[17]:


# To join the Regions in Nigeria from the list of states.
South_south = ['Uyo', 'Rivers']
South_east = ['Imo', 'Anambra', 'Abia']
South_west = ['Oyo', 'Osun', 'Ogun', 'Lagos']
North_west = ['Kastina', 'Kaduna']


# # Tuple
# 
# A tuple is a collection of objects which are ordered and immutable. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
# 
# Creating a tuple is as simple as putting different comma-separated values. Optionally you can put these comma-separated values between parentheses also. An assignment to all of the elements in a tuple using a single assignment statement. Tuple assignment occurs simultaneously rather than in sequence, making it useful for swapping values.

# In[18]:


Nigeria = ("Imo", "Abia", "Anambra", "Lagos", "Uyo", "Rivers", "Ogun", "Oyo", "Osun", "Kaduna")
type(Nigeria)


# In[19]:


# Concatenating in tuple
South_south = ('Uyo', 'Rivers')
South_east = ('Imo', 'Anambra', 'Abia')
South_west = ('Oyo', 'Osun', 'Ogun', 'Lagos')
print(South_south+South_east+South_west)


# In[20]:


# creating nested tuple
South_south = ('Uyo', 'Rivers')
South_east = ('Imo', 'Anambra', 'Abia')
South_west = ('Oyo', 'Osun', 'Ogun', 'Lagos')
Southern_region = (South_south, South_east, South_west)
print(Southern_region)


# In[21]:


#creating a tuple with repetition
South_south = ('Uyo', 'Rivers')*2
print(South_south)


# In[22]:


#Slicing in Tuple
print(Nigeria[1:2])


# In[23]:


print(Nigeria[:2])


# In[24]:


South_east = ('Imo', 'Anambra', 'Abia')
print(len(South_east))


# In[25]:


len(Nigeria) #In Tuple python counts words as a letter


# In[26]:


Nigeria.count("Abia")


# In[27]:


Nigeria.index("Abia")


# In[28]:


list1 = [0, 1, 2]
print(tuple(list1))


# In[29]:


dir(Nigeria)


# # Set
# A Set is an unordered collection of elements that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set. The major advantage of using a set, as opposed to a list, is that it doesn't allow repetitions. This is based on a data structure known as a hash table. Sets are unordered consequently we cannot access items using indexes like we do in lists.

# In[30]:


cookies = {"milk", "flour", "butter", "egg"}
print(cookies)


# In[31]:


#add an element to the list
cookies.add("sugar")
print(cookies)


# In[32]:


cookies = {"sugar", "milk", "flour", "butter", "egg"}
drinks = {"malt", "coke", "fanta", "pepsi"}
brunch = cookies.union(drinks) # union joins the elements together
print(brunch)


# In[33]:


cookies = {"sugar", "milk", "flour", "butter", "egg"}
drinks = {"malt", "coke", "fanta", "pepsi"}
brunch = cookies.intersection(drinks)
print(brunch) # intersection gets the common elements in the list


# In[34]:


cookies & drinks


# In[35]:


cookies - drinks


# In[36]:


cookies.add("honey")
print(cookies)


# In[37]:


cookies_ingredient = {"oil", "baking powder"}


# # Dictionary
# A dictionary is a collection of ordered, changeable items in a curly brackets and do not allow duplicates.
# Dictionaries are used to store data values in key:value pairs.
# Let's see examples

# In[38]:


children = {
    "colour_of_eyes" : "blue", 
    "colour" : "dark", 
    "weight" : 3, 
    "height" : 50}
print(children)


# In[39]:


# To determine how many items a dictionary has, you can use the len() function:
print(len(children))


# In[40]:


print(type(children))


# In[41]:


# get the value of the key
children = {
    "colour_of_eyes" : "blue", 
    "colour" : "dark", 
    "weight" : 3, 
    "height" : 50}
u = children["colour"]
print(u)


# In[42]:


# get the value of the key
u = children.get("colour")
print(u)


# In[43]:


# this will return keys in the dictionary
u = children.keys()
print(u)


# In[44]:


# this will return values in the dictionary
u = children.values()
print(u)


# In[45]:


# to update the list in the dictionary
children["time_of_birth"] = 7.00
print(children)


# In[46]:


# The items() method will return each item in a dictionary, as tuples in a list.
u = children.items()
print(u)


# In[47]:


children = {
    "colour_of_eyes" : "blue", 
    "colour" : "dark", 
    "weight" : 3, 
    "height" : 50}
if "height" in children:
    print('height is one the keys in dictionary')


# In[48]:


children = {
    "colour_of_eyes" : "blue", 
    "colour" : "dark", 
    "weight" : 3, 
    "height" : 50}
children["colour"] : "fair"
print(children)


# In[49]:


# The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
children = {
    "colour_of_eyes" : "blue", 
    "colour" : "dark", 
    "weight" : 3, 
    "height" : 50}
children.update({"colour" : "fair"})
print(children)


# In[50]:


# pop() removes item with the key specified name from the list
children.pop("height")
print(children)


# In[51]:


# popitem() removes the last item from the list
children.popitem()
print(children)


# In[52]:


# del removes item with a specified key name
del children["colour_of_eyes"]
print(children)


# In[53]:


# deletes the items in a list and leaves an empty dictionary
children.clear()
print(children)


# In[54]:


help(children)


# ### Python dir() function
# dir() is a powerful inbuilt function that returns list of the attributes and methods of any object (say functions , modules, strings, lists, dictionaries etc.)
# Syntax : dir({object})

# In[55]:


# getattr() Function
class Shoes:
    shoe_colour = "White"
    shoe_size = 40
    
y = getattr(Shoes, 'shoe_colour')
print(y)


# In[56]:


#The add() method adds an element to the set.
shoe_colour = {"White", "Red", "Brown", "Gold"}
shoe_colour.add("Blue")
print(shoe_colour)


# In[57]:


#The class keyword is used to create a class.
# A class is like an object constructor. Lets see an example below to see how we can use it to create an object.
class bmi:
    height = 1.57
    weight = 60
x = bmi
print(x.height)


# In[58]:


# delattr() function will delete the specified attribute from the specified object.
class bmi:
    height = 1.57
    weight = 60
y = delattr(bmi,'weight')
print(y)


# In[59]:


# The dir() function returns all properties and methods of the specified object, without the values
class bmi:
    height = 1.58
    weight = 65
print(dir(bmi))


# https://www.geeksforgeeks.org/sets-in-python/
# https://www.w3schools.com/python/python_dictionaries_access.asp

# In[ ]:




