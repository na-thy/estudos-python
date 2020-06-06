print('*.*.*.*. PROJETO FINAL DO CURSO DE PYTHON .*.*.*.*')
print('*.*.*.*. NOTAS FINAIS DOS ALUNOS .*.*.*.*')
print('Aluna: Nathaly Rodrigues Madureira Rondon\n')

cadastrados = 0
feminino = 0
masculino = 0
aprovados = 0
aprovadas = 0
exame_m = 0
exame_f = 0 
reprovados = 0
reprovadas = 0

cadastrar_aluno = str(input('Deseja cadastrar aluno: [S/N]: ')).upper()
while cadastrar_aluno not in 'SN':
    print('Opção Inválida.')
    cadastrar_aluno = str(input('Deseja cadastrar aluno: [S/N]: ')).upper()

while cadastrar_aluno == 'S':
    cadastrados +=1
    aluno = input('Informe o nome do aluno(a): ')
    sexo = str(input('Informe o sexo do aluno(a): [F/M]: ')).upper()
    
    while sexo != "M" and sexo != "F":
        print('OPÇÃO inválida.')
        sexo = str(input('Informe o sexo do aluno(a): [F/M]: ')).upper()

        if sexo == 'F':
        feminino +=1
    elif sexo == 'M':
        masculino +=1

    for cont in range(0,3):
        if cont == 0:
            nota1 = float(input('Qual o valor da nota 1: '))
            while nota1 < 0 or nota1 >10:
                nota1 = float(input('Qual o valor da nota 1: '))
        elif cont == 1:
            nota2 = float(input('Qual o valor da nota 2: '))
            while nota2 < 0 or nota2 >10:
                nota2 = float(input('Qual o valor da nota 2: '))
        elif cont == 2:
            nota3 = float(input('Qual o valor da nota 3: '))
            while nota3 < 0 or nota3 >10:
                nota3 = float(input('Qual o valor da nota 3: '))
    
    cadastrar_aluno = str(input('Deseja cadastrar outro aluno: [S/N]: ')).upper()
    while cadastrar_aluno not in 'SN':
        cadastrar_aluno = str(input('Deseja cadastrar outro aluno: [S/N]: ')).upper()

    media = (nota1+nota2+nota3)/3
   
    if media >= 7:
        if sexo == 'F':
            aprovadas += 1
        else:
            aprovados += 1
    elif media >= 4 and media < 7:
        if sexo == 'F':
            exame_f += 1
        else:
            exame_m +=1
    elif media < 4:
        if sexo == 'F':
            reprovadas +=1
        else:
            reprovados +=1

if cadastrados >=1:
    aprov = aprovadas+aprovados
    exam = exame_f+exame_m
    reprov = reprovadas+reprovados

    pct_alunos_aprovados = aprov*100/cadastrados
    pct_alunos_exame = exam*100/cadastrados
    pct_alunos_reprovados = reprov*100/cadastrados
    print("\n")
    print("RESULTADO:")
    print(f"Total alunos cadastrados: {cadastrados}")
    print(f"Total alunos aprovados: {pct_alunos_aprovados:.0f}%")
    print(f"Total alunos em exame: {pct_alunos_exame:.0f}%.")
    print(f"Total alunos reprovados: {pct_alunos_reprovados:.0f}%")
    print(f"Aluna(s) Aprovada(s): {aprovadas}, Exame: {exame_f} e Reprovada(s): {reprovadas}.")
    print(f"Aluno(s) Aprovado(s): {aprovados}, Exame: {exame_m} e Reprovado(s): {reprovados}.\n")

else:
    print("Sistema Finalizado.\n")
