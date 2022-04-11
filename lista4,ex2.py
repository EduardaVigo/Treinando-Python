n = int(input("Infrome a quantidade de alunos: "))

soma = 0
contador = 0
while contador <  n:
    nota = float(input("Digite a nota: "))
    soma = soma + nota
    contador = contador + 1

media = soma / n 
print("A média da turma foi ", media)