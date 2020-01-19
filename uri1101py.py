while True:
    line=input()
    l=line.split(' ')
    n1=int(l[0])
    n2=int(l[1])

    if(n1<=0 or n2<=0):
        break
    sum=0
    if(n1<n2):
        res = ''
        for i in range(n1,n2+1):
            sum +=i
            if(i == n2):
                res += '%d'%i
            else:
                res +='%d '%i
        print(res,"Sum=%d"%sum)
    else:
        res = ''
        for i in range(n2,n1+1):
            sum +=i
            if(i == n1):
                res += '%d'%i
            else:
                res +='%d '%i

        print(res,"Sum=%d"%sum)
    
