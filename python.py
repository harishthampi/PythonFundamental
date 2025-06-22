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