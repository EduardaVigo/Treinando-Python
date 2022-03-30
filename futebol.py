#Entrada de dados
placarA = int(input("Gols do time A:"))
placarB = int(input("Gols do time B:"))

#decidindo resultado
if placarA == placarB:
    print("Empate")
elif placarA > placarB:
    print("Vencedor Time A")
else:
    print("Vencedor Time B")
print("Fim do programa")
