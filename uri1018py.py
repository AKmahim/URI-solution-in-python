list = [100,50,20,10,5,2,1]
n = int(input())
print(n)



for i in range(0,7):
    c = n//list[i]
    n=(n-(c*list[i]))
    l = list[i]
    #print("%d nota(s) de R$ %d,00"%c%l)
    res = "{} nota(s) de R$ {},00"
    result = res.format(c,l)
    print(result)
