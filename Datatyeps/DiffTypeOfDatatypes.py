# Integers

i = 1
print i

i= 1+1
print i

i = "1" + "1"
print i

i = 1 + 4.5
print i

try:
    i = 1 + "1"
    print i
except Exception as e:
   print e

  #o/p=TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Complex numbers
a= 1 + 2j
print a

# Addition of Complex numbers
b = 2 + 3j
print a+b
print a*b

# Single line comment

print "Hello" #it is  half line comment

# Multi line comment
# this is second line

""" Second way of multi line comment
which is triple quotes """

b = 1  +2 +3 +4+6 + \
7+ 8

print b

#string
name1, name2 = "Hello", " World"
print name1 + name2

name1 = "Hello"; name2=  " World"
print name1 + name2

#Type of Operator
print type(name1)
print type(b)
print type(a)

# Is instance Operator
print isinstance(a,complex)
print isinstance(name1, str)


#Multiline String assignment
name3 = '''hello john
          how are you?'''
print name3   # if any indentation or syntext error occurrs entire program will not execute.

#Dictionary datatype
# Understand JSON
# there are main data type is JSObject, Boolean, number ,Array, string Its always follow Key Value pattern
# any JSON either starts with [](denotes Array) / {}(denotes JSObject)

a={"name": "Pretty", 2:"Jhon", "score": 5.6} # it is dict for Python but as normal it is a key value pattern where `name` is key and its value is `Pretty` so for JSON it can be of any type which mention

print a # {2: 'Jhon', 'score': 5.6, 'name': 'Pretty'}

print type(a) # <type 'dict'>

print a["name"] # prints `Pretty`

print a.keys # o/p = <built-in method keys of dict object at 0x10a8bdd70>
print a.values # o/p = <built-in method values of dict object at 0x10a8bdd70>

print a.keys() #o/p = [2, 'score', 'name'] order is int then string
print a.values() #o/p = ['Jhon', 5.6, 'Pretty']

#List datatype

i = [1, "pretty",3.4,-1]

print i     #o/p = [1, 'pretty', 3.4, -1] list can save any type of data

print i[3:] #Slice operator to access the data (from : To-1)

print i[0:2] #o/p = [1, 'pretty']

print i[0:3] # o/p = [1, 'pretty', 3.4]

print i*2  # o/p = [1, 'pretty', 3.4, -1, 1, 'pretty', 3.4, -1]

print i + i  #o/p = [1, 'pretty', 3.4, -1, 1, 'pretty', 3.4, -1]

print type(i) #o/p = <type 'list'>

#Tuple datatype
"""A tuple is a read only datatype we can not modify
   its size and value of the items in it"""

T = (1, 3.4,"pretty","hello", -5, 1.00005)

print T[3:] # o/p = ('hello', -5, 1.00005)

print T[2:5] #o/p = ('pretty', 'hello', -5)

print T+T #o/p = (1, 3.4, 'pretty', 'hello', -5, 1.00005, 1, 3.4, 'pretty', 'hello', -5, 1.00005)

print T*2 #o/p = (1, 3.4, 'pretty', 'hello', -5, 1.00005, 1, 3.4, 'pretty', 'hello', -5, 1.00005)

print type(T) #o/p = <type 'tuple'>
