n = int(input())

y=n//365
print("%d ano(s)"%y)
n=n-(y*365)
m=n//30
print("%d mes(es)"%m)
n=n-(m*30)
d=int(n)
print("%d dia(s)"%d)
