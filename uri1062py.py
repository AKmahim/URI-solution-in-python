count = 0
sm = 0.0
for i in range(1,7):
    n = float(input())
    if(n>0):
        count = count + 1
        sm = sm + n
        
print("%d valores positivos"%count)
resul = sm/count
print("%.1f"%resul)
