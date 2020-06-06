volume = int(input("Volume: "))
if volume < 20:
    print("Está um pouco baixo")
elif 20 <= volume < 40:
    print("Está bom para música ambiente")
elif 40 <= volume < 60:
    print("Perfeito, posso ouvir todos os detalhes")
elif 60 <= volume < 80:
    print("Ótimo para festa")
elif 80 <= volume < 100:
    print("Está muito alto!")
else:
    print("Meus ouvidos doem! :(")
