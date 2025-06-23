# name = input("Enter your Name...")
# print("Hello, " + name)

num = 10
print(type(num))
num = 10.78
print(type(num))
name = 'Harish'
print(type(name))
result = True
print(type(result))
num = [1,2,34,5]
print(type(num))
num = {1,2,34,5}
print(type(num))

long_string = ''' wow
000
---'''
print(long_string)

weather = "It's \"KINDOF\" sunny"
print(weather)

name = 'Johnny'
age = 55
print(f'Hi {name}. You are {age} years old.')
print('Hi {0}. You are {1} years old.'.format(name,age))
name = 'me mem em'
print(name[3])

# name[start:stop:stepover]
name='0123456789'
print(name[0:9:2])
# print(name[::-1]) 9876543210 reverse a string
print(name[-7])

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
quote2 = quote.replace('be','me')
print('quote '+ quote)
print('quote2 '+quote2)




# birth_year = input('What year were you born? ')
# age = 2025 - int(birth_year)
# print(f'Your age is: {age}')

# userName = input('Enter your Username:')
# password = input('Enter your Password:')
# count = len(password)
# hidden_password = '*' * count
# print(f'{userName}, your password {hidden_password} is {count} letters long.')

l1 = [1,2,3,4,5]
l2 = ['apple','b','c']
l3 = [1,2.5,'a',True]
print(f'l1 {type(l1)} l2 {type(l2)} l3 {type(l3)}')

# ListSlicing
amazon_cart = ['notebooks','sunglasses','toys','grapes']
print(amazon_cart[0:4:1])
amazon_cart[0] = 'Laptop'
print(amazon_cart)
sample_cart = amazon_cart
sample_cart[0] = 'pen'
print(f'amazon_cart {amazon_cart} sample_cart {sample_cart}')
sample_cart1 = amazon_cart[:]
sample_cart1[0] = 'penciles'
print(f'amazon_cart {amazon_cart} sample_cart1 {sample_cart1}')

num = [1,2,3,4,5]

num.append(100)
num.insert(1,99)
num.extend([101,102])
print(num)

poped_num = num.pop()
print(poped_num)
num.remove(99)
print(num)
num.clear()
print(num)

basket = ['a','x','b','c','d','e','d']
print('d' in basket)

print(list(range(1,100)))

sentence = '!'.join(['hi','my','name','is','harish'])
print(sentence)

# list unpacking
a,b,c,*other,d = [1,2,3,4,5,6,7,8,9]
print(a,b,c,other,d)

dict = {
    'a':[1,2,3],
    'b':'hello',
    'x':True
}
print(dict['b'])
print (dict.get('age',55))
print (dict.get('a',55))
print('hello' in dict.keys())
print('hello' in dict.values())
print(dict.items())

# Tuple immutable List
my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

# Set
my_set = {1,2,3,4,5,5}
print(my_set)
# print(my_set[0]) error because set is unordered
list1 = [1,2,3,4,5,5]
print(set(list1))

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
# print(my_set.difference(your_set)) output 1 2 3 
# print(your_set.difference(my_set)) output 6 7 8 9 10
# print(my_set.difference_update(your_set))
# print(my_set)
# print(my_set.intersection(your_set))
# print(my_set.isdisjoint(your_set)) 2 sets have same elements or not
# print(my_set.union(your_set)) {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.issubset(your_set)) # my_set is subset of your_set or not
print(your_set.issuperset(my_set))


# if condition:
#    do something
# else:
#    do something else

is_old = False
is_licenced = True

if is_old and is_licenced:
    print("You are old enough to drive")
elif is_licenced:
  print("You can drive now")
else :
    print("You are not old enough to drive")
print("okok")

# Truthy and Falsy
# Falsy values are: 0, None, False, "", [], {}, set(), range(0)

# Ternary operator 
# option_if_true if condition else option_if_false
is_friend = False
can_message = "message allowed" if is_friend else "message not allowed"

print(can_message)

# Short circuiting means that the interpreter will stop evaluating the rest of the expression as soon as it knows the final value.
is_friend = False
is_user =  True
if is_friend and is_user:
  print("Best friends forever")

is_magician = True
is_expert = False

if is_magician and is_expert:
  print("You are a master magician")
elif is_magician:
  print("At least you are getting there")
elif not is_magician:
  print("You need magic powers")


num = [1,2,3,4,5,6,7,8,9,10]

for item in [1,2,3,4]:
    print(item)

# literable - list, dictionary, tuple, set, string 

user = {
  'name':'Golem',
  'age':50,
  'can_swim':False
}
for item in user :
  print(item)
for item in user.keys() :
  print(item)
for item in user.items() :
  print(item)
for item in user.values() :
  print(item)


    # Counter
    my_list = [1,2,3,4,5,6,7,8,9,10]
    count = 0

    for item in my_list:
      count += item
    print(count)


    # range(start,stop,stepover)
    print(range(100)) 
    for num in range(0,100,50):
       print(num)
    for _ in range(0,100,50):
       print("Hello")
    for _ in range(0,100,50):
      print(list(range(10)))

    # enumerate() means index count
    for i,char in enumerate('Hello'):
     print(i,char)
    for i,char in enumerate([1,2,3,4,5]):
     print(i,char)

    for i,char in enumerate(list(range(100))):
      if char == 50:
        print(f'index of 50 is: {i}')

    # while condition:
      # do something
        # break

    i = 0
    while(i<50):
      print(i)
      break
    print('done with all the work')

    continue # continue to next iteration
    pass # do nothing at all
    break # break out of the loop


#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
import re


picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for item in picture:
  print('') # print new line
  for i in item :
         if i==0:
           print(' ',end='')
         elif i == 1:
           print('*',end='') #end='' is used to print in same line


some_list = ['a','b','c','b','d','m','n','n']
# sorted_list = sorted(some_list)
# print(sorted_list)
# temp = ''
result = []
# for item in sorted_list:
#     if temp == item:
#        result.append(item)
#     else:
#        temp = item

# print(result)

for item in some_list:
    if some_list.count(item) > 1:
        if item not in result:
          result.append(item)
print(result)


# Function - def is the keyword for defining a function
def hello ():
  print('helloooooooooooooooooooooo')
hello()

# arguments means the values we pass to the function and parameters means the variables we use inside the function

def say_hello(name): # name is the parameter
  print(f'hello {name}')
  
say_hello('John') # John is the argument

# positional arguments  - means the order of the arguments matters
# keyword arguments - means the order of the arguments does not matter

say_hello(name='Cena') # keyword arguments

# default parameters - means the default value of the parameter is set 
def say_hello(name = 'Kane'):  # default parameter
  print(f'hello {name}')
say_hello()




#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?



def checkDriverAge():
	age = input("What is your age?: ")
	if int(age) < 18:
		print("Sorry, you are too young to drive this car. Powering off")
	elif int(age) > 18:
			print("Powering On. Enjoy the ride!");
	elif int(age) == 18:
			print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkDriverAge(age=0):
	if int(age) < 18:
		print("Sorry, you are too young to drive this car. Powering off")
	elif int(age) > 18:
			print("Powering On. Enjoy the ride!");
	elif int(age) == 18:
			print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(18);



# Methods vs Functions
# Methods are functions that are built into a data type
# list(), print(), max(), min(),input()
# Functions are standalone pieces of code that you can call
# def some_random_stuff()


# DocStrings - means the documentation of the function
def test(a):
    '''
    Info: this function tests and prints param a 
    ''' # this is the docstring
    print(a)
test('abx')

# *args and **kwargs - means the arguments and keyword arguments

def super_func(*args): # *args means the function can take any number of arguments
  print(args)  # args is a tuple (1, 2, 3, 4, 5)
  return sum(args)
print(super_func(1,2,3,4,5))

def super_func(**kwargs):  # **kwargs means the function can take any number of keyword arguments
  print(kwargs)  # kwargs is a dictionary {'num1': 10, 'num2': 205}
super_func(num1=10,num2=205)
# Rule: params, *args, default parameters, **kwargs
def super_func(name,*args,i='hi',**kwargs):
  pass

def highest_even(li):
  highest_evenNumber = 0
  for item in li:
      if item % 2 == 0:
          if highest_evenNumber < item:
              highest_evenNumber = item
  return highest_evenNumber

print(highest_even([10,2,3,4,88,11]))

# Scope - what variables do I have access to?
def total():
  total_score = 100
  print(total_score)
total()
print(total_score) # error because total_score is not defined outside the function
# order of scope - Local Scope, Parent Scope, Global Scope, Built-in - function 

total = 0
def  count():
  global total # global keyword is used to access the global variable
  total+=1
  return total

# nonlocal # nonlocal keyword is used to access the parent scope variable (not a global variable but outside the scope of current function)
x = "global"
def outer():
  x = "local"
  def inner():
    nonlocal x 
    x = "nonlocal" # this will change the value of x in outer function
    print("inner:", x)
  inner()
  print("outer:", x)
outer()
print("global:", x)

# Pure Function - it always produces the same output for the same input and it does not have any side effects 
def sum(num1,num2): 
  return num1 + num2 
print(sum(1,3)) 

import random

def sum_random(num1,num2):  # Non Pure Function because it produces different output for the same input because of random.randint(1, 10)
  return num1 + num2 +random.randint(1, 10)  # random.randint(1, 10) is a side effect because it is not related to the input or output of the function
print(sum_random(1,3)) 

#  map , filter, zip, reduce

#  map(function, iterable) - applies a function to all the items in an iterable. It returns a new list with the results. It does not modify the original list.
print('Map function')
my_list = [1,2,3,4,5]
def multiply_by2(item): 
  return item*2
print(list(map(multiply_by2,my_list)))  
print(my_list)

# filter(function, iterable) - applies a function to all the items in an iterable. It returns a new list with the results. It does not modify the original list. It only returns the items that return True. 
print('Filter function')
my_list = [1,2,3,4,5]
def check_even(item): 
  return item % 2 == 0
print(list(filter(check_even,my_list)))  
print(my_list)

#  zip(iterable1, iterable2) - combines two iterables into one. It returns a new list with the results. It does not modify the original list. 
print('Zip function')
my_list1 = [1,2,3,4,5]
my_list2 = ['a','b','c','d','e']
print(list(zip(my_list1,my_list2)))

 # reduce(function, iterable) - applies a function to all the items in an iterable. It returns a single value. It does not modify the original list. It is a part of the functools module.
print('Reduce function')
from functools import reduce # reduce is a part of the functools module
my_list1 = [1,2,3,4,5]
def accumulator(acc,item):  # acc is the accumulator and item is the current item in the iterable
  # print(acc,item)
  return acc + item  # 0 + 1 = 1, 1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10, 10 + 5 = 15
print(reduce(accumulator,my_list,0)) # 0 is the initial value of the accumulator

# list comprehension - a way to create a new list from an existing list
print('List comprehension')

my_list = []
for char in 'hello':
  my_list.append(char)
print(my_list)

# my_listcomprehension = [param for param in 'hello']
my_listcomprehension = [char for char in 'hello']  # param is the variable that we are using inside the loop
print(my_listcomprehension)

my_list2 = [num for num in range(0,100)]
my_list3 =  [num*2 for num in range(0,100)]  # we can also do some operations on the variable
my_list4 =  [num for num in range(0,100) 
            if num % 2 == 0]  # if condition is true then only the value is added to the list
print(my_list2)
print(my_list3)
print(my_list4)
# set comprehension - a way to create a new set from an existing set
my_set = {char for char in 'hello'}
print(my_set)
my_set2 = {num for num in range(0,100)}
print(my_set2)
my_set3 =  {num for num in range(0,100) 
  if num % 2 == 0}
print(my_set3)
#  dictionary comprehension - a way to create a new dictionary from an existing dictionary
simple_dict = {
  'a':1,
  'b':2
}
my_dict = {key:value ** 2 for key,value in simple_dict.items()} 
print(  my_dict)
my_dict2 = {key:value ** 2 for key,value in simple_dict.items()
           if value % 2 == 0} 
print( my_dict2)
my_dict3 = {num:num*2 for num in [1,2,3]}
print(my_dict3)
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates1= []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates1.append(value)

# print(duplicates1)

duplicates = list({char for char in some_list
             if some_list.count(char) > 1})
print(duplicates)

# Modules in Python are simply Python files with .py extension, which implement a set of functions. Modules are a way of organizing Python code into reusable pieces.

# import - is the keyword for importing a module  - import <module_name>

pycharm - is the IDE for python
Packages in Python are a way of organizing related modules into a single package. Import <package_name>.<module_name>   

Different ways of importing a module -
import <module_name>  - import the whole module
import <module_name> as <alias>  - import the whole module with an alias
from <module_name> import <function_name>  - import a specific function from a module
from <module_name> import *  - import all the functions from a module
from <module_name> import <function_name> as <alias>  - import a specific function from a module with an alias

_init__.py - is the file that makes a directory a package