#dicionario em python

pessoas = {'nome': 'Gustavo', 'sexo': 'masculino', 'idade': '22'}
pessoas['peso'] = 98.5  
for k,v in pessoas.items():
    print(f'{k} = {v}')
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

