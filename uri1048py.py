n = float(input())


def salary(n,p):
    final_salary=n+((n*p)/100)
    salary_incresed=(n*p)/100
    print("Novo salario: %.2f"%final_salary)
    print("Reajuste ganho: %.2f"%salary_incresed)

if(n> 0.00 and n<=400.00):
    salary(n,15)
    print("Em percentual: 15 %")
elif(n> 400.00 and n<=800.00):
    salary(n,12)
    print("Em percentual: 12 %")
elif(n> 800.00 and n<=1200.00):
    salary(n,10)
    print("Em percentual: 10 %")
elif(n> 1200.00 and n<=2000.00):
    salary(n,7)
    print("Em percentual: 7 %")
else:
    salary(n,4)
    printf("Em percentual: 4 %")
