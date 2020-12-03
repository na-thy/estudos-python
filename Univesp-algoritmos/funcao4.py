def h(lst):
    lst[0] = 5
    return lst

myList = [3,6,9,12]
print('lista sem a função:', myList)
h(myList)
print('lista dentro da função alterando o valor do primeiro valor:', h(myList))