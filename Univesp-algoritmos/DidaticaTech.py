class DidaticaTech:
    def __init__(self, v=10, i=1): #metodos são funcoes dentro de uma classe
        self.valor = v #atributos são as variaveis dentro de uma classe
        self.incremento = i
        self.valor_exponencial = v
    def incrementa(self):
        self.valor = self.valor + self.incremento
    def verifica(self):
        if self.valor > 12:
            print('Ultrapassou 12 ')
        else:
            print('Não ultrapassou 12')
    def exponencial(self, e):
        self.valor_exponencial = self.valor**e
    def incrementa_quadrado(self):
        self.incrementa()
        self.exponencial(2)

a = DidaticaTech()
a.incrementa() #chamei o objeto 1 vez 10+1
print('O valor de a', a.valor)
'''a.verifica()
a.incrementa() #chamei o objeto mais uma vez 11+1
print(a.valor)
a.verifica() 
a.incrementa() #chamei o objeto mais uma vez 12+1
print(a.valor)
a.verifica()'''

b = DidaticaTech() 
b.incrementa() #criei um novo atributo b, que não compartilha com o mesmo valor de a 
print('O valor de b', b.valor)
a.exponencial(3)
print('O valor de a',a.valor,'exponencial de 3 é',  a.valor_exponencial)
a.incrementa_quadrado()
print('O valor de a',a.valor,'exponencial de 2 é',  a.valor_exponencial)

class Calculos(DidaticaTech): #herança
    pass

class Calculos(DidaticaTech):
    def __init__(self, d=5):
        super().__init__(v=10, i=1) #invoca a classe principal do valor 
        self.divisor = d
    def decrementa(self):
        self.valor = self.valor - self.incremento
    def divide(self):
        self.valor = self.valor/self.divisor

c = Calculos()
print('o valor de c', c.valor)
c.incrementa()
print('O valor de c incrementado', c.valor) #c somado com o c inicial
c.decrementa()
print('o valor de c decrementado', c.valor)
c.divide()
print('o valor c(10) dividido por 5 =', c.valor)



