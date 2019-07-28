n = input("enter a number:")
i=2
while i<n:
    if n%i ==0:
        break
    i+=1
if i==n:
    print "n is a prime no."
else:
    print "n is not a prime no."
