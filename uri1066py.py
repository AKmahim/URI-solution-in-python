e=0
o=0
p=0
ne=0

for i in range(1,6):
    n = int(input())

    if(n%2 == 0):
        e = e+1
    if(n%2 != 0):
        o +=1
    if(n>0):
        p +=1
    if(n<0):
        ne +=1


print("%d valor(es) par(es)"%e)
print("%d valor(es) impar(es)"%o)
print("%d valor(es) positivo(s)"%p)
print("%d valor(es) negativo(s)"%ne)
