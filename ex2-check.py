numa = float(input("Digite o número de anos: "))
numb = float(input("Digite o número de meses: "))

numc = int (input("Digite o 't': "))

resto = (numb + numc) % 12
div = (numb + numc) // 12
anos = numa + div

print ("O tempo final será de " + str(anos) + " anos e " + str(resto) + " meses.")
