while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n <= 0:
        break
    for i in range(1,11):
        print(f'{n:2} x {i:2} = {n*i}')
