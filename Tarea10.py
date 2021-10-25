numero1 = int(input('Proporciona el numero1: '))
numero2 = int(input('Proporciona el numero2: '))

if numero1 > numero2:
    print(f'El numero mayor es: {numero1}')
elif numero1 < numero2:
    print(f'El numero mayor es: {numero2}')
else:
    print(f'{numero1} y {numero2} son iguales')