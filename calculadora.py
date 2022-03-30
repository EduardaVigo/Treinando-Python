num_a = float(input("Digite o 1° número: "))
num_b = float(input("Digite o 2° número: "))

op = input("Operador (+-*/):")

if op == '+':
    pass
elif op == '-':
    print("resultado", num_a - num_b)
elif op == '*':
    print("resultado", num_a * num_b)
elif op == "/":
    if num_b != 0:
        print("resultado", num_a / num_b)
    else:
        print("Impossível divisão por 0")
else:
    print("Operador não indentificado!") 