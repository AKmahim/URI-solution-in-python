b = 0
T = int(input())
for a in range(2,T+1,2):
    b=a*a
    res='{}^2 = {}'
    print(res.format(a,b))
    b=0
