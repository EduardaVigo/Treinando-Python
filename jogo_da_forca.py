def coloca_traco(word):
    aux = ""
    i = 0
    while i < len(word):
        aux = aux + "_ "
        i = i + 1
    return aux


def verifica(guess, word, secret):
    aux = ""
    i = 0
    while i < len(word):
        if guess == word[i]:
            aux = aux + guess + " "
        else:
            aux = aux + secret[2 * i] + " "
        i = i + 1
    return aux


palavra = "passaro"
erros = 0
segredo = coloca_traco(palavra)

while erros < 6 and "_" in segredo: 
    print(segredo)  
    print("Erros: ", erros)
    chute = input("Letra: ")
    segredo = verifica(chute, palavra, segredo)
    if not chute in palavra:
        erros = erros + 1

if erros >= 6:
    print("Você foi enforcado: ", palavra)
else:
    print("Parabéns, você acertou ", palavra)
