palavras = ['coconut', 'strawberry', 'banana', 'pineapple']
def bubble_sort(palavras):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(palavras)-1):
            if palavras[i] < palavras[i+1]:
                temp = palavras[i]
                palavras[i] = palavras[i+1]
                palavras[i+1] = temp
                swapped = True
bubble_sort(palavras)
print(palavras)