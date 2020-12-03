def BubbleSort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if (v[j]>v[j+1]):
                v[j],v[j+1] = v[j+1],v[j]

def InsertionSort(v):
    for i in range(1,len(v)):
        x = v[i]
        j = i-1
        while j>=0 and x<v[j]:
            v[j+1] = v[j]
            j -= 1
            v[j+1] = x

def MergeSort(v,ini,fim):
    if ini < fim:
        meio = (ini+fim)//2
        MergeSort(v,ini,meio)
        MergeSort(v,meio+1,fim)
        intercala(v,ini,meio,fim)
def intercala(v,ini,meio,fim):
    L = v[ini:meio+1]
    R = v[meio+1:fim+1]
    L.append(99999)
    R.append(99999)
    i=0
    j=0
    for k in range(ini,fim+1):
        if L[i] <= R[j]:
            v[k] = L[i]
            i+=1
        else:
            v[k] = R[j]
            j+=1
            
def QuickSort(v, ini,fim):
    meio = (ini+fim)//2
    pivo = v[meio]
    i = ini
    j = fim
    while i<j:
        while v[i]<pivo:
            i+=1
        while v[j]>pivo:
            j-=1
        if i<=j:
            v[i],v[j] = v[j],v[i]
        i+=1
        j-=1
    if j>ini:
        QuickSort(v,ini,j)
    if i<fim:
        QuickSort(v,i,fim)

def BuscaBinaria(l,x,ini,fim):
    meio = (ini+fim)//2
    if fim < ini:
        print(-1) 
    elif x == l[meio]:
        print(meio)
    elif x < l[meio]:
        print(BuscaBinaria(l,x,ini,meio-1))
    elif x > l[meio]:
        print(BuscaBinaria(l,x, meio+1,fim))


numeros = [1,15,25,7,38,9,45,6,8,5,45,67,27,70,71,43434,4,37]
print(numeros)


BubbleSort(numeros)
print(numeros)

BuscaBinaria(numeros, 45, 0, 16)


'''InsertionSort(numeros)
print(numeros)'''

'''MergeSort(numeros, 0, len(numeros)-1)
print(numeros)'''

'''QuickSort(numeros, 0, len(numeros)-1)
print(numeros)'''

'''print('O número 4 está na lista:',4 in numeros)
print('O número 10 está na lista:',10 in numeros)
print('Qual posição está o número 37 na lista numeros:', numeros.index(37)+1)'''



