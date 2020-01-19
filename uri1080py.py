f = float(input())
h = f

l= []
for n in range(2,101):
    l.append(int(input()))
for n,i in l,range(2,101):
    if(n>h):
        h = n
        p = i
print("%d\n%d"%h %p)
