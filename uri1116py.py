T = int(input())
for i in range(1,T+1):
    line = input()
    l= line.split(' ')
    x= int(l[0])
    y=int(l[1])

    if(y==0):
        print("divisao impossivel")
    else:
        d=x/(y*1.00);
        print("%.1f"%d)
