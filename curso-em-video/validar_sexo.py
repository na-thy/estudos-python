sexo = ' '

while sexo not in 'FM':
    sexo = str(input('Digite o sexo:[F/M] ')).upper()    
    
    if sexo == 'FM':
        break