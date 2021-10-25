valor = int(input('Escribe el valor: '))

valorMinimo = 0
valorMaximo = 5

dentroDeRango = (valor >= valorMinimo) and (valor <= valorMaximo)

if dentroDeRango:
    print(f'El valor {valor} está dentro de rango')
else:
    print(f'El valor {valor} está fuera de rango')
