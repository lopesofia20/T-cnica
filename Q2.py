#Escreva um programa que verifique, em uma string, a existência da letra ‘a’,
#  seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

palavra = input("Digite uma palavra: " )

palavra = palavra.lower()
conta = palavra.count("a")
if 'a' in palavra:
    print(f"A letra A aparece {conta} vezes na palavra informada")
else:
    print("A letra A não existe na palavra informada")