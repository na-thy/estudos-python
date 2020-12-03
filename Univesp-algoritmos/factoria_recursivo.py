def fat(n):
    if n == 0:
        print(1)
        
    else:
        res = n * fat(n-1)
        print(res)

n = input('Digite o valor de n: ')
fat(n)