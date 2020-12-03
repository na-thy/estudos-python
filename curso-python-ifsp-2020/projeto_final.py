print("Projeto Final do Curso de Python da IFSP")
print("Aluna: Nathaly Rodrigues Madureira Rondon\n")

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
        print("Sexo Inválido. Informe sexo: ")
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

def situacao_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Exame"
    else:
        return "Reprovado"

def ler_aluno():
    aluno = {}
    aluno["nome"] = ler_nome()
    aluno["sexo"] = ler_sexo()
    notas_lidas = ler_notas()
    aluno["media"] = calcular_media(notas_lidas)
    aluno["situacao"] = situacao_aluno(aluno["media"])
    return aluno 

def ler_alunos():
    alunos = [] 
    while cadastrar_aluno():
        novo_aluno = ler_aluno()
        alunos.append(novo_aluno)
    return alunos

alunos = ler_alunos()

cadastrados = len(alunos)
aprovados = 0
aprovadas = 0
exame_m = 0
exame_f = 0
reprovados = 0
reprovadas = 0

for aluno in alunos: 
    if aluno["sexo"] == "M":
        if aluno["situacao"] == "Aprovado":
            aprovados += 1
        elif aluno["situacao"] == "Exame":
            exame_m += 1
        else:
            reprovados += 1

    else:
        if aluno["situacao"] == "Aprovado":
            aprovadas += 1
        elif aluno["situacao"] == "Exame":
            exame_f += 1
        else:
            reprovadas += 1
 
if cadastrados >=1:
    aprov = aprovadas+aprovados
    exam = exame_f+exame_m
    reprov = reprovadas+reprovados

    total_alunos_aprovados = aprov*100/cadastrados
    total_alunos_exame = exam*100/cadastrados
    total_alunos_reprovados = reprov*100/cadastrados

    print("." *60)
    print("                         \033[0;1mRESULTADO:\033[m") 
    print("." *60)
    print(f"Alunos Cadastrados:  {cadastrados}")
    print(f"Alunos Aprovados:    {total_alunos_aprovados:.0f}%")
    print(f"Alunos em Exame:     {total_alunos_exame:.0f}%")
    print(f"Alunos Reprovados:   {total_alunos_reprovados:.0f}%\n")
    print(f"Aluna(s) Aprovada(s): {aprovadas}, Aluna(s) em Exame: {exame_f} e Aluna(s) Reprovada(s): {reprovadas}.")
    print(f"Aluno(s) Aprovado(s): {aprovados}, Aluno(s) em Exame: {exame_m} e Aluno(s) Reprovado(s): {reprovados}.")
    print("." *60)
    print("                    \033[0;1mSistema Finalizado.\033[m\n")

else:
    print("." *60)
    print("Nenhum aluno cadastrado.\n")
    print("                    \033[0;1mSistema Finalizado.\033[m\n")