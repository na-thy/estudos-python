print("\033[0;33m=\033[m"*18)
print("  ""\033[1;31mPython's Store\033[m")
print("\033[0;33m=\033[m"*18)

preco = float(input("Preço da compra: R$ "))
print("""FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input("Qual opção: "))
if opcao == 4:
    parcela = int(input("Quantas parcelas: "))

dinheiro_cheque = preco - (preco * 0.10)
vista_cartao = preco - (preco * 0.05)
mais_cartao = (preco * 0.20) + preco

if opcao == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f}".format(preco,dinheiro_cheque))
elif opcao == 2:
    print("Sua compra de R${:.2f} vai custar R${:.2f}".format(preco,vista_cartao))
elif opcao == 3:
    print("Sua compra foi parcelada em 2x de R${:.2f}".format(preco/2))
    print("Sua compra ficou em R${:.2f} sem juros.".format(preco))
elif opcao == 4:
    print("Sua compra foi parcelada em {} vezes no cartão.".format(opcao))
    print("Sua compra de R${:.2f} vai custar R${:.2f} com juros.".format(preco,mais_cartao))
    print("Cada parcela será de R${:.2f}".format(mais_cartao / parcela))
else:
    print("Opção inválida. Tente novamente.")
    