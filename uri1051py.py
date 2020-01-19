a = float(input())

if(a>=0.00 and a<=2000):
    print("Isento")
elif(a>=2000.01 and a<=3000):
    a = a - 2000
    b=a*0.8
    print("R$ %.2f"%b)
elif(a>=3000.01 and a<=4500):
    a = a - 3000
    b=a*0.18+80
    print("R$ %.2f"%b)
else:
    a= a - 4500
    b= a*0.28+350
    print("R$ %.2f"%b)
