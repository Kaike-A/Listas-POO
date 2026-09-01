l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))


if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    
    if l1 == l2 == l3:
      print('O triângulo é equilátero (todos os lados iguais).')
    elif l1 != l2 and l2 != l3 and l1 != l3:
      print('O triângulo é escaleno (todos os lados diferentes).')
    else:
      print('O triângulo é isósceles (dois lados iguais).') #prof nao pediu mas se eu nao colocasse o programa nao ia retornar nada em alguns casos.

else:
    print('Não é um triângulo!')