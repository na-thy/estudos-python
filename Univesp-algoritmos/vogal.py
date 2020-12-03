def imprime_vogais(palavra):
    vogais = ''
    for c in palavra:
        if c in "AaEeIiOoUu":
            vogais += c
    print(vogais)
             
palavra = input('Digite uma palavra: ')
imprime_vogais(palavra)