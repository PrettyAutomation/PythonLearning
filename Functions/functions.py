def test():
    print("Hello world")


test()


def sum01(a, b):
    c = a + b
    return c


S1 = sum01(10, 20)
print(S1)


def get_capital_name(name="India"):
    print(name)
    if name == "India":
        print("New Delhi")
    elif name == "USA":
        print("Washington DC")
    else:
        print("Country is not defined")


get_capital_name("USA")
get_capital_name(100)
get_capital_name()


# Recursive function
def fact(num):
    if num > 1:
        num = num * fact(num-1)
    return num


num01 = input("enter the no. to get the factorial no.")
print(fact(int(num01)))


def get_list_element(list01):
    for x in range(len(list01)):
        if x == 3:
            break
    print('forth position element is: ' + list01[x])


get_list_element(["a", "b", "c", "d", "e"])


# concatenation
def login(username, password):
    print("login with %s and %s" % (username, password))


login("pretty@gmail.com", "active@123")


# multiple arguments
def login(username, password):
    print(username, password)


login(username="pretty@gmail.com", password="test@123")


# *arg
def fun(*arg):
    for x in arg:
        print(x)


fun([2, 45, 23, 44, 56])


# keyword **arg
def key_value_func(**arg):
    for key, value in arg.items():
        print("%s == %s" % (key, value))


key_value_func(naveen=10, pretty=45, sonam=56)


# lambda function
cube = lambda x: x*x*x
print(cube(10))
