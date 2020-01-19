IN = input()

line = IN.split(' ')

n1 = float(line[0])
n2 = float(line[1])
n3 = float(line[2])
n4 = float(line[3])

media=((n1*2)+(n2*3)+(n3*4)+(n4*1) )/10
print("Media: %.1f"%media)

if(media >= 7.0):
    print("Aluno aprovado.")
elif(media <5.0):
    print("Aluno reprovado.")
elif(media >=5.0 and media <=6.9):
    print("Aluno em exame.")
    ex_num = float(input())
    print("Nota do exame: %.1f"%ex_num)
    final_num=(media+ex_num)/2
    if(final_num >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f"%final_num)
     
        
