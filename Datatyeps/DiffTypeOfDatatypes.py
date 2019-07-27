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

a={"name": "Pretty"} # it is dict for Python but as normal it is a key value pattern where `name` is key and its value is `Pretty` so for JSON it can be of any type which mention

print a # {"name": "Pretty"}

print type(a) # <type 'dict'>

print a["name"] # prints `Pretty`
