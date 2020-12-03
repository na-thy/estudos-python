a = 3
b = a 
print(f'A variável B = {b} recebe o valor da variável A = {a}')
print('***' *30)
a = 6
print(f'Alteramos o valor da variável A para {a}, o valor da variável B permanece sendo o valor da variável A do começo do código = {b}')
print('***' *30)

a = [3,4,5]
b = a 
print(a,b)

b[1] = 8
print(a,b)
print('***' *30)

def g(x):
    x = 5
    return x

a = 3
print(f'valor de A na variável = {a}')
g(a)
print(f'valor de A dentro da função g(a) = {g(a)}')
print('***' *30)

def h(lst):
    lst[0] = 5
    return lst

myList = [3,6,9,12]
print(f'Minha lista no começo do código = {myList}')
h(myList)
print(f'Valor da minha lista dentro da função h(lst) alternando o valor da 1 posição na lista = {h(myList)}')