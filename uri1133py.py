x =int(input())
y =int(input())

if(x<y):
    low =x+1
    high=y
else:
    low=y+1
    high=x
for i in range(low,high):
    if(i%5 ==2 or i%5 ==3):
        print("%d"%i)
