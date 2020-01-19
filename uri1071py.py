a = int(input())
b = int(input())

if(a<b):
    s=a
    l=b
else:
    s=b
    l=a


sm=0

if(s%2==0):
    s = s + 1
    for i in range(s,l,2):
        sm = sm + i
else:
    s=s+2
    for i in range(s,l,2):
        sm = sm + i

print("%d"%sm);
