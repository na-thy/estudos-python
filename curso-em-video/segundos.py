segundos_str = input ("Por favor, entre com o número de segundos que deseja converter:")
total_segs = int (segundos_str)

horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segundos_restantes_finais = segs_restantes % 60
print (horas, "horas,", minutos ,"minutos e", segundos_restantes_finais, "segundos.")
