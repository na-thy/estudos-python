x = int(input("Digite um número inteiro: "))
print("""Escolha a base para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal""")
opcao = int(input("Sua opção: "))

if opcao == 1:
    print("{} convertido para Binário é igual {}".format(x, bin(x)[2:]))
elif opcao == 2:
    print("{} convertido para Octal é igual {}".format(x, oct(x)[2:]))
elif opcao == 3:
    print("{} convertido para Hexadecimal é igual {}".format(x, hex(x)[2:]))
else:
    print("Opção inválida")

