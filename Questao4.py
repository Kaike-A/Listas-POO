hipotenusa = int(input('Digite o valor da hipotenusa: '))
cateto1 = int(input('Digite o valor do primeiro cateto: '))
cateto2 = int(input('Digite o valor do segundo cateto: '))

if hipotenusa**2 == cateto1**2 + cateto2**2:
    print('Os valores formam um triângulo retângulo.')
else:
    print('Os valores não formam um triângulo retângulo.')