sexo = ""
while sexo != "F" and sexo != "M":
    sexo = str(input("Informe seu sexo [F/M]: ")).strip().upper()[0]
    if sexo != "F" and sexo != "M":
        print("Dados inválidos. Por favor informe o sexo: ")

print("Sexo {} registrado com sucesso.".format(sexo))
