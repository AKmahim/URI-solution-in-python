IN = input()
line = IN.split(' ')

a = int(line[0])
b = int(line[1])

if(b%a==0 or a%b==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
