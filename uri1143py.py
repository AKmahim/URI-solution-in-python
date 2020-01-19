import math

T =int(input())
for i in range(1,T+1):
    s=math.pow(i,2)
    c=math.pow(i,3)
    res='{} {} {}'
    
    print(res.format(i,int(s),int(c)))
