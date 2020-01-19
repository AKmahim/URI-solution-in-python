T = int(input())

for i in range(1,T+1):
    line = input()
    IN = line.split(' ')
    a = float(IN[0])
    b = float(IN[1])
    c = float(IN[2])
    av=((a*2)+(b*3)+(c*5))/10
    print("%.1f"%av)
