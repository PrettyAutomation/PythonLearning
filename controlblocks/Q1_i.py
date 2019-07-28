n = input("Pattern size:")

for i in range(n):#[0,1,2,3,4]
    print " "*i,
    for j in range(n-i): #[[0,1,2,3,4],[0,1,2,3],...]
       print i+1,
    print ""
