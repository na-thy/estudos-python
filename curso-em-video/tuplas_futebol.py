times = ('Flamengo', 'Santos', 'Palmeiras', 'Atlético-PR', 'Grêmio', 'São Paulo', 
'Corinthians', 'Internacional', 'Fortaleza', 'Goias', 'Atlético', 'Bahia',
'Vasco', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'A classificação do Brasileirão é: {times}')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense na classificação: {times.index("Chapecoense")+1} posição')
print(f'O São Paulo na classificação: {times.index("São Paulo")+1} posição')
