l = int(input("Qual a largura da parede: "))
a = int(input("Qual a altura da parede: "))

a = l*a
tinta = a/2

print("Para pintar essa parede, você precisará de {:.0f} latas de tinta".format(tinta))