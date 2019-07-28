from __future__ import print_function
n = input("Pattern size:")
for i in range(n):
    print((n-i-1)* " ",end='')
    for j in range(i*2+1): #[[0,1,2,3,4],[0,1,2,3],...]
       print('*', end ='')
    print("")

for i in range(n-1)[::-1]:
  print((n-i-1)*" ",end='')
  for k in range(2*i+1):
    print('*', end ='')
  print("")
