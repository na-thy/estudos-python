print(">_<"*10)
print("          ::TABUADA::")
print(">_<"*10)
t = int(input("Digite um número para ver sua tabuada: "))
for x in range(1,11):
    a = x * t
    print("{} x {:2} = {:2}".format(t,x,x*t))