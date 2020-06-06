min = int(input("Tempo em minutos: "))
ano = min // 360
dias = min // 1440
horas = min % 1440
mins = horas // 60
segundos = mins % 60
print("{}anos {}dias {}horas {}minutos {}segundos".format(ano, dias,horas, mins, segundos))
