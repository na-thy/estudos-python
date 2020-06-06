from datetime import date
data = date.today().year
nascimento = int(input("Digite o ano do seu nascimento: "))
print("""Qual seu sexo :
[ 1 ] = Feminino
[ 2 ] = Masculino""")
sexo = int(input("Digite aqui: "))
 
idade = 2019 - nascimento
ano = 18 - idade
alistamento = 2019 + ano

if sexo == 1:
    print("Você não precisa se alistar.")
if  sexo == 2 and idade == 18:
    print("Você tem {} anos em {}.".format(idade,data))
    print("Precisa se alistar IMEDIATAMENTE.")
elif sexo == 2 and idade < 18:
    print("Quem nasceu em {} tem {} anos em {}.".format(nascimento,idade,data))
    print("Ainda faltam {} anos para seu alistamento.".format(ano))
    print("Seu alistamento será em {}.".format(alistamento))
elif sexo == 2 and idade > 18:
    print("Quem nasceu em {} tem {} anos em {}.".format(nascimento,idade,data))
    print("Seu alistamento foi em {}.".format(alistamento))
