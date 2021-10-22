a = int(input('Por favor ingresa un número: '))

residuo = a % 2

if residuo == 0:
    print(f'{a} es un número par')
else:
    print(f'{a} no es un número par')
