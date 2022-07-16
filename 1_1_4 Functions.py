#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# A function is a block of organized, reusable code that is used to perform a single, related action. ... Different programming languages name them differently, for example, functions, methods, sub-routines, procedures, etc.
# 
# Topics we will cover:
# - Defining a Function
# - Passing arguments
# - Using Docstrings
# - Passing multiple arguments/ positional arguments
# - Passing keyword/ named arguments
# - Using default value
# - Returning values, tuple, dictionary
# - Passing arbitrary number of arguments
# - - def make_samosa(size, *fillings):for filling in fillings:
# - Importing functions from other modules

# Function is a group of statements that performs a specific task.
# 
# ## Advantages:
# 
# - Makes your code more organized and manageable.
# - Brings code reusability.
# 
# ## Function Syantax:
# ```
# def <function name>([parameters]):
#     '''Doc string'''
#     Logic/statements
#     ...
#     ...
#     return value/print(value)
# ```
# **def** - marks the start of the function header.\
# **function name** - a unique name to idenfity the function, this naming follows the same checklist we learnt in variable naming.\
# **parameters/arguments** - used to pass a value to the function while calling. These are optional.\
# **Doc String** - a short description about the function. This is optional.\
# **Logic/statements** - one or more valid python statements to perform the required task.\
# **return** - this will return a value from the funxtion. Optional.\
# **print** - to display a value from the fucntion. Optional.

# In[1]:


def my_function():
    print("Hello from a function")


# In[2]:


my_function

Arguments
Value can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

 
def <function name>([argument]):

# In[3]:


def my_function(name):
  print(name + " : Graduate")

my_function("David")
my_function("John")
my_function("Betsy")


# In[5]:


# you can call the functions after you've created one.
my_function("Lovelyn")


# In[6]:


def school(name, level):
    print(name +" :" + level)
school("David","level 1")


# In[8]:


school("Joy","level 2")


# In[9]:


def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# #### Arbitrary Arguments, *args
# You can add * for more arguements in your function.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# 
# def function name (argument1,argument2):
# 
# def function name ( *args ):

# In[10]:


def my_function(*cars):
    print("We have the newest model of cars: " + cars[0])

my_function("SUV", "Ford", "Benz")


# In[11]:


def my_function(car1, car2, car3):
    print("The Model of these cars have the following colors : " + car3)

my_function(car1 = "black", car2 = "ash", car3 = "blue")


# #### Arbitrary Keyword Arguments, **kwargs
# You can add ** for more keyword arguments that will be passed into your function before the parameter name in the function definition. This way the function will receive a dictionary of arguments, and can access the items accordingly
# 
# def function name (** keyword argument):

# In[12]:


def my_function(**cars):
    print("The Models have the following colors: " + cars["Ford"])

my_function(SUV = "black", Ford = "blue")


# In[13]:


def my_function(CAR = "black"):
  print("The colour of my car is: " + CAR)

my_function("blue")
my_function("ash")
my_function()
my_function("coffee")


# #### Passing a List as an Argument
# You can pass a list, string, number, dictionary as an arguement and it will be treated as the same data type.
# 
# def function name (argument1,argument2, ** keywordargument):
# 
#     pass

# In[14]:


def my_function(animals):
    for x in animals:
        print(x)

domestic_animals = ["cat", "dog", "pig"]

my_function(domestic_animals)


# #### Return Values
# This will return a value from the funxtion. Optional.

# In[19]:


def my_function(a):
  return 5 * a

print(my_function(2))
print(my_function(3))
print(my_function(6))


# # Examples of Functions
# Let's see more examples and practice exeercises

# In[18]:


def sum(x,y):
    z = x + y
    print(z)
x = 5
y = 4
sum(x,y)


# In[11]:


# grades of scores for Mathematics
n = [80,85,67,46,50,75,90,67]
mean(n)


# In[30]:


n = [80,85,67,46,50,75,90,67]
def variance(n):
    N = len(n)
    mean = sum(n)/N
    deviations = [(x - mean) ** 2 for x in n]
    variance = sum(deviations)/n
    return variance


# In[33]:


# variance doesn't work without introducing numpy
import numpy as np
n = [80,85,67,46,50,75,90,67]
n = np.array([80,85,67,46,50,75,90,67])
variance(n)


# In[44]:


def stdev(n):
    import math
    var = variance(n)
    std_dev = math.sqrt(var)
    return std_dev


# #### Quick Task: Create a Loan Interest Calculator Using Compound Interest
# 
# 1. Ask user to enter Total Price, Downpayment, Rate of Interest (rate per year), Time Duration (years)
# 2. Compute Compound Interest 
# 3. Return the amount the user will pay

# In[31]:


pow (2,3)


# In[32]:


principle =int(input("enter the total price:"))
rate =int(input("enter the rate:"))
time =int(input("enter the time:"))
Amount = principle * (pow((1 + rate / 100), time))
CI = Amount - principle
print("Compound interest is", CI)


# In[3]:


principle = int(input("enter the initial principle balance: "))
rate = int(input("enter the rate: "))
time = int(input("enter the time: "))
Amount = principle * (pow((1 + rate / 100), time))
CI = Amount - principle
print("Compound Interest is: ", CI)


# In[5]:


def calculate_compound_interest(p, r, t):
    CI = p * pow((1+r/100),t)
    return CI

p = 200000
r = 3
t = 12
calculate_compound_interest(p, r, t)


# In[7]:


def find_amount(amount, time):
    amounting = amount/(time*12)
    return amounting

amount = 40000
time = 5
find_amount(amount, time)


# In[10]:


loan_rate = {"car":8, "education":9, "home":7.5, "personal":13.5}

def calculate_compound_interest_amount(p, r, t):
    a = p*pow((1+r/100),t)
    return a

def find_emi(amount, time):
    return amount/(time*12)
def process_loan(name, purchase_amount, downpayment, category="personal", time=5):
    principle = purchase_amount-downpayment
    rate = loan_rate[category]
    amount = calculate_compound_interest_amount(principle, rate, time)
    emi = find_emi(amount,time)
    print (rate)
    print (amount)
    print (emi)

process_loan("Ajay", 800000, 200000, "education")


# In[2]:


def list_counter(mylst):
    this_dict=dict()
    for i in mylst:
        if i in this_dict:     # i in this_dict.keys()
            this_dict[i]+=1
        else:
            this_dict[i]=1
    return this_dict

input_list=[1,2,3,4,5,6,3,4,5,3,4,4,3,5,3,5,3,1,3,4,55]    
results = list_counter(input_list)


# In[3]:


results


# In[1]:


def numerics_counter(numbers):
    numec = dict()
    for i in numbers:
        if i in numec:
            numec[i]+=1
        else:
            numec[i] = 1
    return numec

numbers = [1,2,2,3,4,4,8,9,7,4,3,6,7,48]
check_numbers = numerics_counter(numbers)


# In[3]:


check_numbers = numerics_counter(numbers)
check_numbers


# In[7]:


def list_counter(mylist):
    this_dict = dict()
    for i in mylist:
        if i in this_dict:
            this_dict[i]+=1
        else:
            this_dict[i]=1
    return this_dict

input_list = [1,2,3,3,2,2,2,5,5,5,23,23,1,1]
results = list_counter(input_list)

results


# In[11]:


input_list = ['a','a','d','d','d','e','t','t','y','y','e']
list_counter(input_list)


# # Find countries in Africa which starts or ends with a letter in a string 
# Let's see examples to show:

# In[24]:


Countries_in_africa = ["Angola","Tanzania","Bostwana","Nigeria","South_africa","kenya","senegal"]
statement = "These are countries in Africa "+" ".join(Countries_in_africa)+" today"
statement

sentence = statement.split(" ")

letter_store = dict()

for letters in sentence:
    letters = letters.lower()
    starting_letter = letters[0]
    ending_letter = letters[-1]
    
    if starting_letter not in letter_store:
        letter_store[starting_letter] = set()
    if ending_letter not in letter_store:
        letter_store[ending_letter] = set()
    letter_store[starting_letter].add(letters)
    letter_store[ending_letter].add(letters)


# In[25]:


letter_store


# In[28]:


def word_counter(mystr, given_letter = "e"):
    count = 0
    print (given_letter)
    for word in mystr.split(' '):
        if word[0].lower() == given_letter.lower():
            count += 1
            continue
        if word[-1].lower() == given_letter.lower():
            count += 1
    return count
word_counter("engine egg lemon")


# In[1]:


loan_rate = {"car":8, "education":9, "home":7.5, "personal":13.5}
loan_database = dict()

def calculate_compound_interest_amount(p, r, t):
    a = p*pow((1+r/100),t)
    return a

def find_emi(amount, time):
    return amount/(time*12)

def process_loan(name, purchase_amount, downpayment, category="personal", time=5):
    principle = purchase_amount-downpayment
    rate = loan_rate[category]
    amount = calculate_compound_interest_amount(principle, rate, time)
    emi = find_emi(amount,time)
    if name in loan_database:
        print ("Sorry you already have a pending loan")
        return
    my_loan_rec = {"emi":emi, "balance":amount}
    loan_database[name] = my_loan_rec
    
process_loan("Ajay", 800000, 200000, "car")
process_loan("Shivani", 200000, 0, "personal", time=1)


# In[2]:


process_loan("Shivani", 200000, 0, "personal", time=1)


# In[6]:


process_loan("Ajay", 800000, 200000, "personal")


# In[ ]:




