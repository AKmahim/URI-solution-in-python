n = int(input())

h = n/3600
m = n%3600/60
s = n%60
res = "{}:{}:{}"
print(res.format(int(h),int(m),int(s)))
