n =int(input())
for i in range(1,n+1):
    res='{} {} {}'
    print(res.format(i,i*i,i*i*i))
    res1='{} {} {}'
    print(res1.format(i,i*i+1,i*i*i+1))
