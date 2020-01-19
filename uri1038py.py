IN = input()

line = IN.split(' ')

c = int(line[0])
n = int(line[1])

if(c==1):
    res=4.00*n
    print("Total: R$ %.2f"%res)
    
elif(c==2):
    res = 4.50*n
    print("Total: R$ %.2f"%res)
    
elif(c==3):
    res = 5.00*n
    print("Total: R$ %.2f"%res)

elif(c==4):
    res = 2.00*n
    print("Total: R$ %.2f"%res)
        
elif(c==5):
    res = 1.50*n
    print("Total: R$ %.2f"%res)
        
