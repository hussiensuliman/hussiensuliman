s=input()
n=len(s)
y=[]
z=0
for x in range (n):
    if s[x]=='1':
       y.append(1)
    else:
        y.append(0)
for x in range (n):
  z=y[x]*2**(n-1-x)+z
print (z)     