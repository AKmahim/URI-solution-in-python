sum = 0
count=0
n =float(input())
if(n==1):
    print("novo calculo (1-sim 2-nao)")
    sum=0.00
    count=0
if(n<0 and n>10):
    print("nota invalida")
else:
    while True:
        n=float(input())
        if(n>=0 and n<=10):
            sum +=n
            count +=1
            if(count==2):
                count=0
                sum=0
