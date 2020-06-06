completa = lambda nome,sobrenome: nome.strip().title()+ " "+sobrenome.strip().title()

primeiro = str(input('Informe o primeiro nome: '))
segundo = str(input('Informe o segundo nome: '))

print(completa(primeiro,segundo))