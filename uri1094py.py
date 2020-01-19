rabbit=0
rat = 0
frog = 0
total = 0

T = int(input())

while T:
    line=input()
    IN=line.split(' ')
    n = int(IN[0])
    ch = IN[1]

    total += n

    if(ch == 'C'):
        rabbit = rabbit + n
    elif(ch == 'R'):
        rat = rat + n
    elif(ch == 'S'):
        frog += n
    T -= 1
print("Total: %d cobaias"%total)
print("Total de coelhos: %d"%rabbit)
print("Total de ratos: %d"%rat)
print("Total de sapos: %d"%frog)
r1=(rabbit/total)*100
r2=(rat/total)*100
r3=(frog/total)*100
print("Percentual de coelhos: %.2f"%r1,'%')
print("Percentual de ratos: %.2f"%r2,'%')
print("Percentual de sapos: %.2f"%r3,'%')
