n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

n1 = n1*2
n2 = n2*3
n3 = n3*4

media = (n1+n2+n3+n4)/10
print("Media:","{:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media <= 4.9:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    notaexame = float(input())
    print("Nota do exame:","{:.1f}".format(notaexame))
    notaexame = (notaexame+media)/2
    if notaexame >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:","{:.1f}".format(notaexame))
