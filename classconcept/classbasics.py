class Test:
    pass

    # A sample method
    @staticmethod
    def fun():
        print("Hello")


# Driver code
obj = Test()
obj.fun()


class Car:
    pass
# the variable which defines in the class called class variable
    wheels = 4

# Every method and constructor will have "self" parameter
    def __init__(self):
        print("i am in default constructor")

# Python will consider the latest constructor
    def __init__(self, color):
        print("i am in default constructor")
        self.color = color
        print(self.color)

    @staticmethod
    def test():
        print("test method")

# variable defined inside the method called instance variable
    def __init__(self, price):
        self.price = price
        print(self.price)


# creating object of the class
c1 = Car("Red")
print(c1.wheels)
c1.test()
c1 = Car(1000)


