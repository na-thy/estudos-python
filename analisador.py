homem = ""
idadehomem = 0
lista_idade = []
mulheres_20 = 0
for c in range (1,5):
    print("=-"*10)
    print("     {}ª PESSOA  ".format(c))
    print("=-"*10)
    nome = str(input("NOME: "))
    idade = int(input("IDADE: "))
    sexo = str(input("[M/F]: ")).lower()
    lista_idade.append(idade)
    
    if idade < 20 and sexo == "f":
        mulheres_20 += 1
    elif sexo == "m" and idade > idadehomem:
        idadehomem = idade
        homem = nome
        
print("A média da idade do grupo é {}".format(sum(lista_idade)/4))
print("O homem mais velho tem {} anos e se chama {}.".format(idadehomem,homem))
print("Ao todo são {} mulheres com menos de 20 anos.".format(mulheres_20))
