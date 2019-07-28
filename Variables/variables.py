# simple variable of different types
stringvar= "Pretty"
print stringvar
a = 10
print a

b = 4.05
print b

c = 30.0000000009777 # memory dependent float precision
print c  # it will print 30.000000001


d = 0x12c
print d  # output = 300 (16^2*1 + 16^1*2 + 16^0*c (c hexvalue =12) = 300)

#Reassignmnet of variables

name = "Jhon"
print name

name = "Nick"
print name

name = 10
print name

name = 4.5
print name

name = 300.000000000056
print name

try:
  print Temp # o/p = NameError: name 'Temp' is not defined
except Exception as e:
    print e

#Special Literal

Temp = None
print Temp
