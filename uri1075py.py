n = int(input())
print("2")
for i in range(1,10001):
    if(i%n ==0):
        res = i+2
        print("%d"%res)
