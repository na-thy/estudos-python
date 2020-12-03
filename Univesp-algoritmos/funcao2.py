def juros(preco,juros):
    res = preco * (1+(juros/100))
    return res

print(juros(10,50))
