import math 
eps=0.01
x=0.2
i=1
s=0
z=1
while math.fabs(z)>eps:
    s=s+z
    i=i+2
    z=math.sin(i*x)/i
s=s-1
print(s)
