nome = str(input("Digite seu nome: ")).strip()
nome1 = nome.split()

print("Prazer em te conhecer {}!".format(nome))
print("Seu primeiro nome é: {}".format(nome1[0]))
print("Seu último nome é: {}".format(nome1[len(nome1)-1]))

