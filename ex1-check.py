AulaSeman = float(input("Digite o número de aulas semanais: "))
horaAula = float(input("Digite o valor da hora aula: "))

salarioBase = AulaSeman * 4.5 * horaAula

horaAtividade = salarioBase * 0.05

DSR = (salarioBase + horaAtividade) * (1/6)

salarioMensal = salarioBase + horaAtividade + DSR

print ("O salário base é de " + str(salarioBase))
print ("O valor da hora atividade é de " + str(horaAtividade))
print ("O valor do DSR (Descanso Semanal Remunerado) é de " + str(DSR))
print ("O valor do salário mensal é de " + str(salarioMensal))






