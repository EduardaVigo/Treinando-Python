num = int(input("Digite um número inteiro positivo: "))
divisor = 1
while divisor <= num:
    if num % divisor == 0:
        print (divisor)
    divisor = divisor + 1    
