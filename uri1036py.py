import math
IN = input()

line = IN.split(' ')

a = float(line[0])
b = float(line[1])
c = float(line[2])

d=(math.pow(b,2)-(4*a*c));
if(a!=0 and d>0):
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("R1 = %.5lf"%r1)
    print("R2 = %.5lf"%r2)
    
else:
     print("Impossivel calcular")
    
