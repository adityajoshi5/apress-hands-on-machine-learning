#!/usr/bin/env python
# coding: utf-8

# # Control Flow
# 
# A program’s control flow is the order in which the program’s code executes. The control flow of a Python program is regulated by conditional statements, loops, and function calls. This section covers the if statement and for and while loops; functions are covered in the next class.
# 
# ![](https://www.researchgate.net/profile/Kay_Smarsly/publication/322509045/figure/fig1/AS:583153716215809@1516046088625/Control-flow-of-elementary-control-structures.png)
# 
# # The if Statement
# 
# Often, you need to execute some statements only if some condition holds, or choose statements to execute depending on several mutually exclusive conditions. The Python compound statement if, which uses if, elif, and else clauses, lets you conditionally execute blocks of statements. 
# 
# ## Comparision Operators
# - x == y
# - x!= y
# - x < y
# - x <= y
# - x > y
# - x >= y
# 
# ## Python Indentation
# In Python, the code blocks are defined by a set of common or consistent number of spaces. This is called Python Indentation.
# 
# The block scope will end at the first un-indented line.
# The best practice is to use on Tab space.

# In[1]:


a = 10
b = 5
if b < a:
    print("b is less than a")


# In[2]:


a = 40
b = 28
if b > a:
    print("b is greater than a")
elif b < a:
    print("b is less than a")


# In[3]:


a = 40
b = 28
if b > a:
    print("b is greater than a")
elif b == a:
    print("b is equal to a")
else:
    print("b is less than a")


# In[4]:


# basketball points for each team
tiger = 85
lions = 87
personal_best = 80

if tiger > personal_best and lions > personal_best:
    print("Congratulations! the teams have broken the world championship record")


# In[5]:


# basketball points for each team
tiger = 50
lions = 40
personal_best = 80

if tiger < personal_best or lions < personal_best:
    print("the teams can do better")


# In[6]:


# nested if statemebts: are statements that have if statements inside if statements.

tiger = 85
lions = 87
personal_best = 80

if tiger > personal_best: 
    print("the tiger team has a new personal best")
if lions > personal_best:
    print("the lions team has a new personal best")
else:
    print("No team has exceeded the world record")


# In[7]:


games = ["football", "basketball", "volleyball", "badminton","handball","jockey","tabletennis"]
coaches =["Sylvester", "Captain","Michael","John","Israel","David","Winifred"]
age_limit = [35,34,33,30,40,30,32]


# In[8]:


sports = input("Enter your the sports you love:  ")
if sports in games:
    print("Welcome to sporting teams")
else:
    print("The sport selected is not available")


# In[9]:


sports = input("Enter your the sports you love:  ")
if sports in games:
    print("Welcome to sporting teams")
else:
    print("The sport selected is not available")
sport_coaches = input("Enter the name of your coach ")
if sport_coaches in coaches:
    print("You're in the right place")
else:
    print("Get to know your coach")


# In[10]:


sports = input("Enter your the sports you love:  ")
if sports in games:
    print("Welcome to sporting teams")
elif sports not in games:
    print("Check again and choose your sports")
else:
    print("The sport selected is not available")


# In[11]:


sporting_agelimit = 40
if sporting_agelimit >= 40:
    print("You have a year to play with the team")
elif sporting_agelimit > 40:
    print("You are to discontinue from playing for the team")
else:
    print("We wish you goodluck in your future endeavors")


# # Convert Marks to Grade
# 1. Ask user to enter marks
# 2. Check type of marks object, convert type if required
# 3. Based on standard grading rules, print the grade
# 
# A: 90-100\
# B: 80-90\
# C: 60-80\
# D: 40-60\
# F: Below 40
# 

# In[12]:


marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A Grade")
elif marks < 90 and marks >= 80:
    print("B Grade")
elif marks < 80 and marks >= 60:
    print("C Grade")
elif marks < 60 and marks >= 40:
    print("D Grade")
else:
    print("Fail")


# # Let's create a Simple Interest Calculator
# We will create more mathematical calculators with simple formulars. let's see examples

# Area of a Circle = 3.142 * r * r

# In[14]:


r = int(input("Enter radius of the circle: "))
t = 3.142
Area = t * r * r
print("Area of a circle = ", Area)


# In[15]:


import math


# In[16]:


Area = int(input("Enter the area of a circle: "))
t = 3.142
r = math.sqrt(Area/t)
print("The radius of a circle: \n", r)


# In[17]:


p=int(input("enter principal amount: "))
t=int(input("enter time period: "))
r=int(input("enter rate of interest: "))

SI=(p*t*r)/100
print ("Simple interest = ", SI)
print ("Amount is: "+str(p+SI))


# In[18]:


rate = {"housing": 6, "education":3,"vacation":7}
loan_purpose = input ("why do you need the loan: ")
rate_of_interest = rate[loan_purpose]
print("rate is " + str(rate_of_interest))
principle = int ( input("Enter Principle Amount ") )
time = int ( input("Enter Time Duration ") )

simple_interest = principle * rate_of_interest * time/100
amount = principle+simple_interest
print ("Interest is: {} amount is: {}".format(simple_interest, amount))


# In[19]:


rate = {"housing": 6, "education":3,"vacation":7}
print("Welcome to Global Bank. Pick from categories of loan we offer: ")
for purpose in rate.keys():
    print("/n " + purpose)
loan_purpose = input ("What do you need the loan for: ")
if loan_purpose not in rate:
    print("Sorry, we don't have loans in that category")
rate_of_interest = rate[loan_purpose]
print ("Your rate of interest is "+str(rate_of_interest))
principle = int ( input("Enter Principle Amount ") )
time = int ( input("Enter Time Duration ") )

simple_interest = principle * rate_of_interest * time/100
amount = principle+simple_interest
print ("Interest is {} amounting to {}".format(simple_interest, amount))


# # The while Statement
# 
# The while statement in Python supports repeated execution of a statement or block of statements that is controlled by a conditional expression. 
# 
#     count = 0
#     while x > 0:
#       x = x // 2            # truncating division
#       count += 1
#     print "The approximate log2 is", count
#     
# First, expression, which is known as the loop condition, is evaluated. If the condition is false, the while statement ends. If the loop condition is satisfied, the statement or statements that comprise the loop body are executed. When the loop body finishes executing, the loop condition is evaluated again, to see if another iteration should be performed. This process continues until the loop condition is false, at which point the while statement ends.
# 
# The loop body should contain code that eventually makes the loop condition false, or the loop will never end unless an exception is raised or the loop body executes a break statement. A loop that is in a function’s body also ends if a return statement executes in the loop body, as the whole function ends in this case.

# In[20]:


i = 1
while i < 7:
  print(i)
  i += 1


# In[21]:


i = 1
while i < 21:
    print(i)
    i *= 3


# In[22]:


i = 2
while i % 20:
    print(i)
    i += 2


# In[23]:


i = 1
while i < 6:
    print(i)
    if i == 2:
        break
    i += 2


# In[24]:


i = 0
while i < 8:
    i += 3
    if i == 2:
        continue
    print(i)


# In[25]:


i = 1
while i < 6:
    print(i)
    i += 2
else:
    print("okay")


# In[26]:


# Program to add natural numbers
m = int(input("enter m: "))

#initialize sum and counter
sum = 0
i = 1

while i <= m:
    sum = sum + i
    i = i + 1   # update counter
    
print(sum)


# In[27]:


counter = 0

while counter < 3:
    print("hello")
    
    counter = counter + 1
else:
    print("hi")


# # The for Statement
# 
# The for statement in Python supports repeated execution of a statement or block of statements that is controlled by an iterable expression.
# 
#     for target in iterable:
#       statement(s)
#       
# Note that the in keyword is part of the syntax of the for statement and is functionally unrelated to the in operator used for membership testing.      
# 
# iterable may be any Python expression suitable as an argument to built-in function iter, which returns an iterator object (explained in detail in the next section). target is normally an identifier that names the control variable of the loop; the for statement successively rebinds this variable to each item of the iterator, in order. The statement or statements that comprise the loop body execute once for each item in iterable (unless the loop ends because an exception is raised or a break or return statement is executed).

# In[28]:


Games = ["football", "table_tennis", "volleyball"]
for x in Games:
    print(x)


# In[29]:


Games = ["football", "table_tennis", "volleyball"]
for x in Games:
    print(x)
    if x == "table_tennis":
        break


# In[30]:


Games = ["football", "table_tennis", "volleyball"]
for x in Games:
    if x == "table_tennis":
        break
    print(x)


# In[31]:


# Repeat
sentence = "hi, you look good"

words = sentence.split()
emptydictionary = dict()
for word in words:
    if word in emptydictionary:
        emptydictionary[word] += 1
    else:
        emptydictionary[word] = 1
        
for key,value in emptydictionary.items():
    print(key+" : "+str(value))


# ### The range() Function
# This is a loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
# and ends at a specified number.

# In[33]:


for x in range(6):
  print(x)


# In[34]:


# this specifies the starting number and ending number
for x in range(3, 8):
  print(x)


# In[35]:


# this specifies that the starting number is 2, with the increment of 4 and ends in 30
for x in range(2, 30, 4):
  print(x)


# In[36]:


for x in range(6):
  print("I'm Betsy")
else:
  print("Done")


# In[37]:


for x in range(10):
    if x == 5: break
    print(x)
else:
    print("Done")


# In[38]:


# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "blue", "velvet"]
fruits = ["car", "cloth", "bags"]

for x in adj:
    for y in fruits:
        print(x, y)


# In[39]:


a = int(input("Enter a number : "))
if a <= 30:
    for i in range(1,25):
        print("{} x {} = {}".format(a,i,a*i))
else:
    print("you have exceeded the limit")


# In[40]:


num = int(input("Enter your number "))  

for i in range(1,13):  
   print(num, 'x', i, '=',num*i)


# In[41]:


series=[1, 4, 5, 6, 7]
even_count=0
odd_count=0
for number in series:
    if number % 2 == 0:
        even_count += 1 # even_count = even_count + 1
    else:
        odd_count += 1
print("even count is : {} and odd count is : {}".format(even_count, odd_count))


# In[42]:


import string

vowels = ['a','e','i','o','u']
consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l']


consonents = set(string.ascii_lowercase).difference(set(vowels))
print(consonents)


# In[43]:


import string
print(vowels)


# In[44]:


print(consonents)


# In[45]:


import string

vowels = ['a','e','i','o','u']
consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l']


consonents = set(string.ascii_lowercase).difference(set(vowels))
consonents

v_count = 0
c_count = 0

sentence = input("Enter Sentence: ")
sentence = sentence.lower()
for c in sentence:
    if c in vowels:
        v_count += 1
    if c in consonents:
        c_count += 1

print ("Vowels : "+str(v_count) + ", Consonents : "+str(c_count) )


# In[46]:



v_count = 0
c_count = 0
sentence = input("Make a sentence: ")
sentence = sentence.lower()
for x in sentence:
    if x in vowels:
        v_count += 1
    if x in consonents:
        c_count += 1
        
print("Vowels : " + str(v_count) + ", Consonents : " + str(c_count))


# In[47]:


mylst = [2,4,7,3,8,9,1,2,12,45,67,89]

num = int (input("What's the number you want to search: "))
# without using in keyword

for n in mylst:
    if num == n:
        print ("number is present")
        break
    print ("We are in the loop with number "+str(n))
print ("The loop is over")


# In[48]:


mylst = [2,4,7,3,8,0,9,1,2,12,45,67,12,89]

num = int (input("What's the number you want to search: "))
# without using in keyword

count = 0
for n in mylst:
    if num == n:
        count += 1
print ("The number "+str(num)+" is present "+str(count)+" times ")


# # Number Guessing Game

# In[49]:


# 123456
secret_number = 42

guess = int (input("Enter your Guess: "))
if guess == secret_number:
    print ("You win the game")
else:
    print ("Sorry")


# In[50]:


import random
secret_number = random.randint(1,100)
print(secret_number)


# In[51]:


secret_number = random.randint(1,100)
count = 0
while True:
    guess = int (input("Enter your Guess: "))
    if guess == secret_number:
        print ("You win the game")
        break
    else:
        if guess < secret_number:
            print ("No. Try a higher number")
        if guess > secret_number:
            print ("No. Try a lower number")
    count += 1
print ("Congratulations.. you did it in {} tries".format(count))


# In[ ]:




