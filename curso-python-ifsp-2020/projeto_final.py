def cadastrar_aluno():
    cadastro = input("Deseja cadastrar novo aluno: [S] ou [N]: ").upper()
    while cadastro != "S" and cadastro != "N":
        cadastro = input("Cadastro Inválido: Cadastrar novo aluno: [S] ou [N]").upper()
    return cadastro == "S"

def ler_nome():
    return input("Nome do Aluno: ")

def ler_sexo():
    sexo = input("Qual o sexo: ").upper()
    while sexo != "F" and sexo != "M":
        print('Sexo Inválido. Informe sexo: ')
        sexo = input("Qual o sexo: ").upper()
    return sexo

def ler_notas():
    notas = [ ]
    for n in range(1,4):
        nota = float(input("Qual o valor da {}ª nota: ".format(n)))
        while nota <0 or nota >10:
            print("Valor Inválido: Informe a nota: ")
            nota = float(input("Qual o valor da nota: "))
        notas.append(nota) 
    return notas 

def calcular_media(notas):
    soma = 0

    for nota in notas:
       soma += nota
    
    return soma / len(notas)

def ler_aluno():
    aluno = {}
    aluno["nome"] = ler_nome()
    aluno["sexo"] = ler_sexo()
    notas_lidas = ler_notas()
    aluno["media"] = calcular_media(notas_lidas)
    return aluno 

def ler_alunos():
    alunos = [] 
    while cadastrar_aluno():
        novo_aluno = ler_aluno()
        alunos.append(novo_aluno)
    return alunos

def print_aluno(aluno):
    print(aluno)

print(ler_aluno())
print(ler_alunos())



