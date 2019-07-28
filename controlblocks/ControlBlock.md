### Type of ControlBlock

#### IF Else
##### syntax
```
if <Expression>:
  <if block>
else:
  <else block>
```

the following code will throw error

###### code:
```
if:
  print "Test If"
```
###### o/p:
```
SyntaxError: invalid syntax
```
###### Why:

there is empty expression in if statement

> Learning: Can't have empty expression if statement

E.g.
```
Map = input("Enter a Map:")
print type(Map)
print Map
if Map["name"]:
    print "name key is available in the Map"
else:
    """
    these block is unreachable
    """
    print "name key is not in the Map"  

```
#### Type of Functions For List

The following code will return the no. of times "pretty" value is present
in the given List
```
Map.values().count("pretty")
```
The following code will return the no. of times "name" Key is present
in the given List
```
number.keys().count("name")
```

#### Different code and there output
1.

*Code:*
```
x= None
if x = 3 :
    print "Test If block"
```
*Output:*
```
if x = 3 :
     ^
SyntaxError: invalid syntax
```

2.

*Code:*
```
if x == 3 :
    print "Test If block"
```
*Output:*
```
NameError: name 'x' is not defined
```
3.

Code:
```
x = None
if x["name"] == 3 :
    print "Test If block"
```
Output:
```
TypeError: 'NoneType' object has no attribute '__getitem__'
```
4.

Code:
```
name="name"
Map = input("Enter a Map:")
print type(Map)
print Map
if Map["name"]:
     print "name key is available in the Map"
```
if input is:
```
Enter a Map:{name:"Pretty"}
```
Output:
```
name key is available in the Map
```
if input is:
```
Enter a Map:{1:"Pretty"}
```
Output:
```
KeyError: 'name'
```

#### Else IF Ladder

##### syntax
```
if <Expression>:
  <if block>
elif <Expression>:
  <elif block>
else:
  <else block>
```

#### For loop

##### syntax
```
for <element> in <List>:
  <for block for each element in list>
```

##### Running for loop without index
```
cities = ["kolkata","Delhi","Mumbai","Bangalore"]
for city in cities:
  print city
```

##### Running for loop with index
```
cities = ["kolkata","Delhi","Mumbai","Bangalore"]
for i in range(len(cities)):
  print cities[i]
```

#### While loop

##### syntax
```
while <Condition>:
 <While block >
```
##### break statement

```
cities = ["kolkata","Delhi","Mumbai","Bangalore"]
for i in range(len(cities)):
  print cities[i]
  break
```
Output:
```
kolkata
```  
```
cities = ["kolkata","Delhi","Mumbai","Bangalore"]
for i in range(len(cities)):
  print cities[i]
  if i == 2:
   break
```
Output
```
kolkata
Delhi
Mumbai
```
```
Note: break can be used only inside the loop, else it will throw the
SyntaxError: 'break' outside loop
```
### continue statement
```
continue statement will not execute the current iteration and execute the next.
```
```
cities = ["kolkata","Delhi","Mumbai","Bangalore"]
for i in range(len(cities)):
  if i == 2:
   continue
  print cities[i]
```
Output:
```
kolkata
Delhi
Bangalore
```
##### Practice Question

- Q1. Try to draw following patterns input will be n

   i) n=5
```
  1  1  1  1  1  
    2  2  2  2
      3  3  3
        4  4
          5
```

    ii) n=5
```
  1  2  3  4  5
    1  2  3  4
      1  2  3
        1  2
          1
```

    iii) n=3
    ```
       *
      ***
     *****
      ***
       *
    ```
- Q2. Find whether given number is prime or not
