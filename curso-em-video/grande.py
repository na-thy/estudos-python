valor = int(input("Digite um valor a ser somado: "))

soma = 0 

while valor > 0:
    digito = valor % 10
    soma = soma + digito
    valor = (valor-digito)//10
    
print ("A soma do valor digitado é: ", soma)