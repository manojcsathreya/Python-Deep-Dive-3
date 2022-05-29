'''
Dictionary Elements

basic structure of dictionary elements: key : value

value ->any Python object integer custom class or instance
function module any Python object…

key ->any hashable object

not all objects are hashable

lists are never hashable

strings are hashable

->hash tables require hash of an object to be constant (for the life of the program)
roughly: immutable objects are hashable
mutable objects are not hashable
more subtle than that… 
---------------------------------------------------------------------------------------


Hashable Objects

Python function: hash(obj) ->some integer (truncated based on Python build: 32-bit, 64-bit)
sys.hash_info.width
->Exception TypeError: unhashable type

->list ->mutable collection ->not hashable

->tuples ->immutable collection ->hashable only if all elements are also hashable

->strings ->immutable collection ->hashable

->int, float, complex, binary, Decimal, Fraction, … ->immutable ->hashable

->set, dictionary ->mutable collections ->not hashable

->frozenset ->immutable collection ->elements are required to be hashable ->hashable

->functions ->immutable ->hashable
->custom classes and objects ->maybe
---------------------------------------------------------------------------------------
Requirements

If an object is hashable:
->the hash of the object must be an integer value
->if two objects compare equal (==), the hashes must also be equal

later ->creating our own custom hashes
->we will also need to conform to these rules

Important: two objects that do not compare equal may still have the same hash
(hash collision)
->more hash collisions ->slower dictionaries
---------------------------------------------------------------------------------------

Creating Dictionaries: Literals

This is a very common way of creating dictionaries

{ key1: value1,
key2: value2,
key3: value3 }

Keys:any hashable object 
Values: any object
{'john': ['John', 'Cleese', 78],
(0, 0): 'origin',
'repr': lambda x: x ** 2,
'eric': {'name': 'Eric Idle',
'age': 75}
}

---------------------------------------------------------------------------------------


Creating Dictionaries: Constructor
dict(key1=value1, key2=value2, key3=value3)

must be a valid identifier name
(think variable, function, class name, etc) any object
dictionary key will then be a string of that name

dict(john=['John', 'Cleese', 78],
repr=lambda x: x ** 2,
eric={'name': 'Eric Idle',
'age': 75},
twin=dict(name='Eric Idle', age=75)
)

{'john': ['John', 'Cleese', 78],
(0, 0): 'origin',
'repr': lambda x: x ** 2,
'eric': {'name': 'Eric Idle',
'age': 75}
}

---------------------------------------------------------------------------------------
Creating Dictionaries: Comprehensions

Just like we can build lists using list comprehensions
or generators using generator expressions (comprehension syntax)
->build dictionaries using dictionary comprehensions
->same basic syntax ->enclosed in {}
->elements must be specified as key: value (if not, you'll be creating a set!)

{str(i): i ** 2 for i in range(1, 5)} -> {'1': 1, '2': 4, '3': 9, '4': 16}
{str(i): i ** 2 
for i in range(1, 5)
if i % 2 == 0}

-> {'2': 4, '4': 16}

---------------------------------------------------------------------------------------

Soapbox!
d = {i: i** 2 for i in range(1, n)}
vs
d = {}
for i in range(1, n):
d[i] = i ** 2

But when things get more complex…
d = {}
url = 'http://localhost/user/{id}'
for i in range(n):
    response = requests.get(url.format(id=i))
    user_json = response.json()
    user_age = int(user_json['age'])
    if user_age >= 18:
        user_name = user_json['fullName'].strip()
        user_ssn = user_json['ssn']
        d[user_ssn] = user_name

=================================================================================================

Creating Dictionaries: fromkeys()

->class method on dict

->creates a dictionary with specified keys all assigned the same value

d = dict.fromkeys(iterable, value)
iterable:
any iterable
contains the keys
hashable elements
value:
all set to same value
optional ->Noneif not provided

d = dict.fromkeys(['a', (0,0), 100], 'N/A')
-> {'a': 'N/A', (0,0): 'N/A', 100: 'N/A'}

d = dict.fromkeys((i**2 for i in range(1, 5)), False)
-> {1: False, 4: False, 9: False, 16: False
=================================================================================================
'''
#Creating Python Dictionaries
#There are different mechanisms available to create dictionaries in Python.

#Literals
#We can use a literal to create a dictionary:

a = {'k1': 100, 'k2': 200}
a #{'k1': 100, 'k2': 200}
type(a) #dict
print(a) #{'k1': 100, 'k2': 200}
# =============================================================================
# Note that the order in which the items are listed in the literal is maintained when listing out the elements of the dictionary. This does not hold for Python version earlier than 3.6 (practically, version 3.5).
# 
# Another thing to note is that dictionary keys must be hashable objects. Associated values on the other hand can be any object.
# 
# So tuples of hashable objects are themselves hashable, but lists are not, even if they only contain hashable elements. Tuples of non-hashable elements are also not hashable.
# =============================================================================

hash((1, 2, 3)) #2528502973977326415
d = {(1,2,3):'This is a tuple'}
d #{(1, 2, 3): 'This is a tuple'}

t1 = (1,2,3)
t2 = (1,2,3)

t1 == t2 #True
t1 is t2 #False
hash(t1) == hash(t2) #True



hash([1, 2, 3])
# =============================================================================
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-4-84d65be9aa35> in <module>
# ----> 1 hash([1, 2, 3])
# 
# TypeError: unhashable type: 'list'
# =============================================================================

hash(([1, 2], [3, 4]))
# =============================================================================
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-5-f578847ae11e> in <module>
# ----> 1 hash(([1, 2], [3, 4]))
# 
# TypeError: unhashable type: 'list'
# 
# So we can create dictionaries that look like this:
# =============================================================================

a = {('a', 100): ['a', 'b', 'c'], 'key2': {'a': 100, 'b': 200}}
a #{('a', 100): ['a', 'b', 'c'], 'key2': {'a': 100, 'b': 200}}
#Interestingly, functions are hashable:

def my_func(a, b, c):
    print(a, b, c)
hash(my_func)
#284093589
#Which means we can use functions as keys in dictionaries:

d = {my_func: [10, 20, 30]}
#A simple application of this might be to store the argument values we want to use to call the function at a later time:

def fn_add(a, b):
    return a + b

def fn_inv(a):
    return 1/a
​
def fn_mult(a, b):
    return a * b
funcs = {fn_add: (10, 20), fn_inv: (2,), fn_mult: (2, 8)}
#Remember that when we iterate through a dictionary we are actually iterating through the keys:

for f in funcs:
    print(f)
# =============================================================================
# <function fn_add at 0x10eeec8c8>
# <function fn_inv at 0x10eeec6a8>
# <function fn_mult at 0x10eeec620>
# We can then call the functions this way:
# =============================================================================

for f in funcs:
    result = f(*funcs[f])
    print(result)
# =============================================================================
# 30
# 0.5
# 16
# We can also iterate through the items (as tuples) in a dictionary as follows:
# =============================================================================

for f, args in funcs.items():
    print(f, args)
# =============================================================================
# <function fn_add at 0x10eeec8c8> (10, 20)
# <function fn_inv at 0x10eeec6a8> (2,)
# <function fn_mult at 0x10eeec620> (2, 8)
# So we could now call each function this way:
# =============================================================================

for f, args in funcs.items():
    result = f(*args)
    print(result)
# =============================================================================
# 30
# 0.5
# 16
# Using the class constructor
# We can also use the class constructor dict() in different ways:
# 
# Keyword Arguments
# =============================================================================
d = dict(a=100, b=200)
d #{'a': 100, 'b': 200}
# =============================================================================
# The restriction here is that the key names must be valid Python identifiers, since they are being used as argument names.
# 
# We can also build a dictionary by passing it an iterable containing the keys and the values:
# =============================================================================

d = dict([('a', 100), ('b', 200)])
d #{'a': 100, 'b': 200}
#The restriction here is that the elements of the iterable must themselves be iterables with exactly two elements.

d = dict([('a', 100), ['b', 200]])
d #{'a': 100, 'b': 200}
#Of course we can also pass a dictionary as well:

d = {'a': 100, 'b': 200, 'c': {'d': 1, 'e': 2}}
#Here I am using a dictionary that happens to contain a nested dictionary for the key c.

#Let's look at the id of d:

id(d)
#4545038016
#And let's create a dictionary:

new_dict = dict(d)
new_dict
{'a': 100, 'b': 200, 'c': {'d': 1, 'e': 2}}
#What's the id of new_dict?

id(new_dict)
#4545071576
#As you can see, we have a new object - however, what about the nested dictionary?

id(d['c']), id(new_dict['c'])
#(4545357864, 4545357864)
# =============================================================================
# As you can see they are the same - so be careful, using the dict constructor this way essentially creates a shallow copy.
# 
# We'll come back to copying dicts later.
# 
# Using Comprehensions
# We can also create dictionaries using a dictionary comprehension. This is very similar to list comprehensions or generator expressions.
# 
# Suppose we have two iterables, one containing some keys, and one containing some values we want to associate with each key:
# =============================================================================

keys = ['a', 'b', 'c']
values = (1, 2, 3)
#We can then easily create a dictionary this way - the non-Pythonic way!

d = {}  # creates an empty dictionary
for k, v in zip(keys, values):
    d[k] = v
d #{'a': 1, 'b': 2, 'c': 3}
#But it is much simpler to use a dictionary comprehension:

d = {k: v for k, v in zip(keys, values)}
d #{'a': 1, 'b': 2, 'c': 3}
#Dictionary comprehensions support the same syntax as list comprehensions - you can have nested loops, if statements, etc.

keys = ['a', 'b', 'c', 'd']
values = (1, 2, 3, 4)
​
d = {k: v for k, v in zip(keys, values) if v % 2 == 0}
d #{'b': 2, 'd': 4}
#In the following example we are going to create a grid of 2D coordinate pairs, and calculate their distance from the origin:

x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)
#If you remember list comprehensions, we would create all possible (x,y) pairs using nested loops (a Cartesian product):

grid = [(x, y) 
         for x in x_coords 
         for y in y_coords]
# =============================================================================
# grid
# [(-2, -2),
#  (-2, -1),
#  (-2, 0),
#  (-2, 1),
#  (-2, 2),
#  (-1, -2),
#  (-1, -1),
#  (-1, 0),
#  (-1, 1),
#  (-1, 2),
#  (0, -2),
#  (0, -1),
#  (0, 0),
#  (0, 1),
#  (0, 2),
#  (1, -2),
#  (1, -1),
#  (1, 0),
#  (1, 1),
#  (1, 2),
#  (2, -2),
#  (2, -1),
#  (2, 0),
#  (2, 1),
#  (2, 2)]
# import math
# We can use the math module's hypot function to do calculate these distances
# =============================================================================

math.hypot(1, 1)
#1.4142135623730951
#So to calculate these distances for all our points we would do this:

grid_extended = [(x, y, math.hypot(x, y)) for x, y in grid]
grid_extended
# =============================================================================
# [(-2, -2, 2.8284271247461903),
#  (-2, -1, 2.23606797749979),
#  (-2, 0, 2.0),
#  (-2, 1, 2.23606797749979),
#  (-2, 2, 2.8284271247461903),
#  (-1, -2, 2.23606797749979),
#  (-1, -1, 1.4142135623730951),
#  (-1, 0, 1.0),
#  (-1, 1, 1.4142135623730951),
#  (-1, 2, 2.23606797749979),
#  (0, -2, 2.0),
#  (0, -1, 1.0),
#  (0, 0, 0.0),
#  (0, 1, 1.0),
#  (0, 2, 2.0),
#  (1, -2, 2.23606797749979),
#  (1, -1, 1.4142135623730951),
#  (1, 0, 1.0),
#  (1, 1, 1.4142135623730951),
#  (1, 2, 2.23606797749979),
#  (2, -2, 2.8284271247461903),
#  (2, -1, 2.23606797749979),
#  (2, 0, 2.0),
#  (2, 1, 2.23606797749979),
#  (2, 2, 2.8284271247461903)]
# We can now easily tweak this to make a dictionary, where the coordinate pairs are the key, and the distance the value:
# =============================================================================

grid_extended = {(x, y): math.hypot(x, y) for x, y in grid}
grid_extended
# =============================================================================
# {(-2, -2): 2.8284271247461903,
#  (-2, -1): 2.23606797749979,
#  (-2, 0): 2.0,
#  (-2, 1): 2.23606797749979,
#  (-2, 2): 2.8284271247461903,
#  (-1, -2): 2.23606797749979,
#  (-1, -1): 1.4142135623730951,
#  (-1, 0): 1.0,
#  (-1, 1): 1.4142135623730951,
#  (-1, 2): 2.23606797749979,
#  (0, -2): 2.0,
#  (0, -1): 1.0,
#  (0, 0): 0.0,
#  (0, 1): 1.0,
#  (0, 2): 2.0,
#  (1, -2): 2.23606797749979,
#  (1, -1): 1.4142135623730951,
#  (1, 0): 1.0,
#  (1, 1): 1.4142135623730951,
#  (1, 2): 2.23606797749979,
#  (2, -2): 2.8284271247461903,
#  (2, -1): 2.23606797749979,
#  (2, 0): 2.0,
#  (2, 1): 2.23606797749979,
#  (2, 2): 2.8284271247461903}
# Using fromkeys
# The dict class also provides the fromkeys method that we can use to create dictionaries. This class method is used to create a dictionary from an iterable containing the keys, and a single value used to assign to each key.
# =============================================================================

counters = dict.fromkeys(['a', 'b', 'c'], 0)
counters
#{'a': 0, 'b': 0, 'c': 0}
#If we do not specify a value, then None is used:

d = dict.fromkeys('abc')
d #{'a': None, 'b': None, 'c': None}
#Notice how I used the fact that strings are iterables to specify the three single character keys for this dictionary!

#fromkeys method will insert the keys in the order in which they are retrieved from the iterable:

d = dict.fromkeys('python')
d #{'p': None, 'y': None, 't': None, 'h': None, 'o': None, 'n': None}
#Uh-Oh!! Looks like the ordering didn't work!! I've pointed this out a few times already, but Jupyter (this notebook), uses a printing mechanism that will order the keys alphabetically.

#To see the real order of the keys in the dict we should use the print statement ourselves:

print(d)
#{'p': None, 'y': None, 't': None, 'h': None, 'o': None, 'n': None}
#Much better! :-)

