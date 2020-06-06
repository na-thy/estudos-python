nome = str(input("Digite seu nome: ")).strip()

print("Analisando seu nome.....")
print("Nome maiúsculo: {}.".format(nome.upper()))
print("Nome minusculo: {}.".format(nome.lower()))
print("Quantas letras tem {}? Tem {} letras.".format(nome,len(nome) - nome.count(" ")))
separa = nome.split()
print("Quantas letras tem o primeiro nome {}? Tem {} letras.".format(nome,len(separa[0])))
