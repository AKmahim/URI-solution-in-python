IN = input()
line = IN.split(' ')

a = float(line[0])
b = float(line[1])
c = float(line[2])

if ((a < (b+c)) and (b < (a+c)) and (c < (b+a))):
    res = a+b+c
    print("Perimetro = %.1f"%res)

else:
    area=0.5*(a+b)*c;
    print("Area = %.1f"%area)
    
