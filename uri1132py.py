a=int(input())
b=int(input())

sum=0
if(a<b):
    for i in range(a,b+1):
        if(i%13 !=0):
            sum +=i
    print("%d"%sum)
else:
    for i in range(b,a+1):
        if(i%13 !=0):
            sum +=i
    print("%d"%sum)
