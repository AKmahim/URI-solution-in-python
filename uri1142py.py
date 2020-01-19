p=4
c=1
T=int(input())
for i in range(1,T+1):
    res=''
    for j in range(c,p+1):
        if(j%4==0):
            res +='PUM'
        else:
            res +='%d '%j
    print(res)
    c +=4
    p +=4
