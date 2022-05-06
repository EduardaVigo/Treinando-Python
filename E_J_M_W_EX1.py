qtd = int(input("Digite o 'n': "))

cont = 0
numAtual = 0
numAnterior = 0

while qtd > 0:
        num = int(input("Digite um número: "))
        numAtual = num
        if num != numAnterior :
                cont = cont + 1        
                numAnterior = numAtual
        qtd = qtd - 1
        
print (cont)