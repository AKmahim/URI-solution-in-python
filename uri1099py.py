T=int(input())
for i in range(1,T+1):
    line=input()
    l=line.split(' ')
    x=int(l[0])
    y=int(l[1])


    if(x<y):
        low=x
        high=y
    else:
        low=y
        high=x
    sum=0
    low +=1
    for j in range(low,high):
        if(j%2 !=0):
            sum +=j
    print("%d"%sum)
