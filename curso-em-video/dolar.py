real = float(input("Quantos reais você tem: R$ "))

dolar = real / 4.11
libra = real / 5.05
euro = real / 4.51

print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(real,dolar))
print("Com R$ {:.2f} você pode comprar £$ {:.2f}".format(real, libra))
print("Com R$ {:.2f} você pode comprar €$ {:.2f}".format(real, euro))