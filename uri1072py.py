T = int(input())
In=0
out=0

l=[]
for n in range(1,T+1):
    l.append(input())
for n in l:
    if(int(n)>=10 and int(n)<=20):
        In +=1
    else:
        out +=1
print("%d in"%In)
print("%d out"%out)
