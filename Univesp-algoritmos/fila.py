fila = [10, 20, 30, 40, 50]
print(fila)
'''fila.append(60)  # insere um elemento no final da fila
print(fila)
print(fila.pop(0)) # remove o primeiro elemento da lista
print(fila)
print(fila.pop(0)) # remove o primeiro elemento da lista
print(fila)
print(fila.pop(0)) # remove o primeiro elemento da lista
print(fila)'''

class Fila(object):
    def __init__(self):
        self.dados = []
 
    def insere(self, elemento):
        self.dados.append(elemento)
 
    def retira(self):
        return self.dados.pop(0)
 
    def vazia(self):
        return len(self.dados) == 0

import fila
f = fila.Fila()
f.insere(10)
f.insere(20)
f.insere(30)
print(f.retira())
print(f.retira())


