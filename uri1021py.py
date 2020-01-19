devider1 = [100.00,50.00,20.00,10.00,5.00,2.00]
devider2 = [1.00,0.50,0.25,0.10,0.05,0.01]

n = float(input())

print("NOTAS:")
for i in range(0,6):
    c = n//devider1[i]
    n=(n-(c*devider1[i]))
    res = "{} nota(s) de R$ %.2f"%devider1[i]
    print(res.format(int(c)))
print("MOEDAS:")

for j in range(0,6):
    c1 = n//devider2[j]
    n = (n-(c1*devider2[j]))
    res = "{} moeda(s) de R$ %.2f"%devider2[j]
    print(res.format(int(c1)))
