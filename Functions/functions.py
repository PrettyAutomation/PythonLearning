# def test():
#     print "Hello world"
# test()
#
# def sum(a,b):
#     c = a + b
#     return c
# S1 = sum(10,20)
# print S1
#
# def getCapitalName(name= "India"):
#     print name
#     if name == "India":
#       print "New Delhi"
#     elif (name == "USA"):
#        print "Washington DC"
#     else:
#        print "Country is not defined"
#
#
# getCapitalName("USA")
# getCapitalName(100)
# getCapitalName()
#
# #Recursive function
# def fact(number):
#     if(number>1):
#       number = number*fact(number-1)
#     return number
#
# number = input("enter the no. to get the facorial no.")
# print fact(number)
#
# #list
#
# def getListElement(list):
#     for x in range(len(list)):
#       if(x==3):
#             break
#       print list[x]
#
# getListElement(["a","b","c","d","e"])
#
# #concatenation
#
# def login(username,password):
#     print("login with %s and %s" %(username,password))
#
# login("pretty@gmail.com","active@123")

# multiple arguments

def login(username, password):
    print(username,password)
login(username= "pretty@gmail.com",password = "test@123")
login("pretty@gmail.com","test@123")

#*arg

def fun(*arg):
    for x in arg:
        print x

fun([2,45,23,44,56])

##keyword **arg

def keyValueFunc(**arg):
    for key,value in arg.items():
        print("%s == %s" %(key,value) )

keyValueFunc(naveen=10,pretty=45,sonam=56)


#lambda function

cube = lambda x: x*x*x
print cube(10)
