### Non Parameter function
```
def test():
    print "Hello world"
test()

o/p = Hello world
```
### Parameter function with return
```
def sum(a,b):
    c = a + b
    return c
S1 = sum(10,20)
print S1

o/p = 30
```
### Default/Optional Parameter function
```
def getCapitalName(name= "India"):
    print name
    if name == "India":
      print "New Delhi"
    elif (name == "USA"):
       print "Washington DC"
    else:
       print "Country is not defined"

getCapitalName("USA")
getCapitalName(100)
getCapitalName()

o/p = USA
      Washington DC
      100
      Country is not defined
      India
      New Delhi
```
### Recursive function
```
def fact(number):
    if(number>1):
      number = number*fact(number-1)
    return number

number = input("enter the no. to get the facorial no.")
print fact(number)

o/p = enter the no. to get the facorial no.4
24

Note:if you press enter without giving input error will be thrown
SyntaxError: unexpected EOF while parsing
which means  the end of your source code was reached before all code blocks were completed

```
### function using list
```
def getListElement(list):
    for x in range(len(list)):
      if(x==3):
            break
      print list[x]

getListElement(["a","b","c","d","e"])

o/p = a
      b
      c
```
### Concatenation in function
```
def login(username,password):
    print("login with %s and %s" %(username,password))

login("pretty@gmail.com","active@123")

o/p = login with pretty@gmail.com and active@123
```

### multiple arguments
```
def login(username, password):
    print(username,password)

login(username= "pretty@gmail.com",password = "test@123")
login("pretty@gmail.com","test@123")

o/p = ('pretty@gmail.com', 'test@123')
      ('pretty@gmail.com', 'test@123')
```
### *arg
```
def fun(*arg):
    for x in arg:
        print x

fun([2,45,23,44,56])

o/p = [2, 45, 23, 44, 56]

```
### keyword **arg
```
def keyValueFunc(**arg):
    for key,value in arg.items():
        print("%s == %s" %(key,value) )

keyValueFunc(naveen=10,pretty=45,sonam=56)

o/p = sonam == 56
      pretty == 45
      naveen == 10

```
### lambda function
```
cube = lambda x: x*x*x

print cube(10)

o/p = 1000

```
