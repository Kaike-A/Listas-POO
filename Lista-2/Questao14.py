frase = input("Digite uma frase: ")
palavras = frase.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] = contagem_palavras[palavra] + 1
    else:
        contagem_palavras[palavra] = 1

for palavra, quantidade in contagem_palavras.items():
    print(f"{palavra}: {quantidade}")