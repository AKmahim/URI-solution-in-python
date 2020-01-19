IN = input()
line = IN.split(' ')

start_h = int(line[0])
start_m = int(line[1])
end_h = int(line[2])
end_m = int(line[3])

d_h=end_h-start_h

if(d_h<0):
    d_h=24+(end_h-start_h)

d_m=end_m-start_m
if(d_m<0):
    d_m=60+(end_m-start_m)
    d_h = d_h - 1

if(start_h==end_h and start_m==end_m):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    
else:
    res = 'O JOGO DUROU {} HORA(S) E {} MINUTO(S)'
    print(res.format(d_h,d_m))
