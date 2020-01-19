line = input()
l =line.split(' ')
x=int(l[0])
y=int(l[1])
c=0
res=''
for i in range(1,y+1):
    c +=1
    if(c==x):
        res +='%d'%i
    else:
        res +='%d '%i
    
    if(c==x):
        c=0
        res +='\n'
print(res)
