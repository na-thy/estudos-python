print("-*"*15)
print(" "*11,"\033[4;36mMÉDIA\033[m")
print("-*"*15)
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota:  "))
print("-*"*15)

media = (n1+n2)/2

if media >= 7.0:
    print("A média do aluno foi \033[0;32m{}\033[m.".format(media))
    print("Ele está \033[1;32mAPROVADO\033[m.")
elif media >= 5.0 and media <= 6.9:
    print("A média do aluno foi \033[0;33m{}\033[m.".format(media))
    print("Ele está de \033[0;33mRECUPERAÇÃO\033[m.")
else:
    print("A média do aluno foi \033[0;31m{}\033[m.".format(media))
    print("Ele está \033[0;31mREPROVADO\033[m.")
