### Sample of Class syntax in python
```
class Test:

    # A sample method
    def fun(self):
        print("Hello")

# Driver code
obj = Test()
obj.fun()

o/p = Hello
```
### Class with constructor and method
```
class car:
# the variable which defines in the class called class variable
    wheels = 4
# Every method and constructor will have "self" parameter
    def __init__ (self):
         print "i am in default constructor"

# Python will consider the latest constructor
    def __init__ (self, color):
         print "i am in default constructor"
         self.color = color
         print self.color

    def test(self):
        print("test method")

# variable defined inside the method called instance variable
    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        return self.price

# crearing object of the class
c1 = car("Red")
print c1.wheels
c1.test()
c1.setPrice(1000)
print c1.getPrice()

o/p = i am in default constructor
      Red
      4
      test method
      1000
```
