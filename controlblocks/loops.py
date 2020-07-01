# For Loop
list01 = input("enter the value for list")
print(list01)
for i in range(6):
    print(list01[i])
else:
    print("list is over")

    
# For Loop with if and break statement
cities = ["kolkata","Delhi","Mumbai","Bangalore"]
for index in range(len(cities)):
    print(cities[index])
    if cities[index] == "Delhi":
        break

# For Loop with if and continue statement
cities = ["kolkata","Delhi","Mumbai","Bangalore"]
for index in range(len(cities)):
    if cities[index] == "Mumbai":
        continue
    print(cities[index])

# while loop
count = 0
while count <= 3:
    print ("hello world")
    count += 1
else:
    print ("Bye world")


# normal for loop





