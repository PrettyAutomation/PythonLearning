# IF Else Block
# if False:
#     number = None
#     number = input("Enter a Number:") #input function will type cast given string but raw_input will not
#     number1 = raw_input("Enter the value:")
#     print type(number)
#     print type(number1) # always will be str
#     print number
#     if number%2 == 0:
#         print "Number is even"
#     else:
#         print "Number is odd"
#
# if False:
#          number = input("Enter a Map:")
#          print type(number)
#          print number
#          if number.keys().count("name") > 0:
#              print "name key is available in the Map"
#          else:
#               print "name key is not in the Map"
#
# if False:
#     name="name"
#     Map = input("Enter a Map:")
#     print type(Map)
#     print Map
#     if Map["name"]:
#          print "name key is availbale in the Map"
#     else:
#          print "name key is not in the Map"
#
# if False:
#     name= "name"
#     Map = input("Enter a Map:")
#     print type(Map)
#     print Map
#     if Map.values().count("pretty")>0:
#         print "pretty value is availbale in the Map"
#     else:
#         print "pretty value is not in the Map"
#
# if False:
#     x = (3,4,"pretty",-2)
#     print x[0]
#     if x[0] == 3 :
#         print "Test If block"
#
#
# #### If Else Ladder
#
# Number = input("Enter the number:")
#
# if Number % 2 == 0:
#     print "Number is divisible by 2"
#
# elif Number% 5 == 0:
#     print "Number is divisible by 5"
#
# elif Number % 10 == 0:
#     print "Number is divisible by 10"
# else:
#     print "Number does not have 0 at the unit position"

# e.g. for str method and f string

a = 10
b = 500
c = 100

if a > b and a > c:
    print("a is highest number")
elif b > c:
    print("b is highest number")
else:
    print("c is highest number")

total = input("enter the value of total: ")
if int(total) < 100:
    print(total+20)
elif 100 > total < 500:
    print(total+50)
else:
    print(total+100)

print(total)
print("total" + str(total))
print("my total value is {total}")
