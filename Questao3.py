n = float(input('Digite um número N real e positivo: '))
x = float(input('Digite um número X real e positivo: '))

if n < 0 or x < 0:
    print('Número inválido. Digite um número real e positivo.')
else:
    print(f'Valor de n elevado x: {n ** x:.0f}')