c=0
s=0
while True:
    if(c==2):
        break
    n = float(input())
    if(n>=0 and n<=10):
        s +=n
        c +=1
    else:
        print("nota invalida")
r =s/2.00
print("media = %.2f"%r)
