calificacion = int(input('Proporciona un valor entre 0 y 10: '))
nota = ''

if calificacion == 10 or calificacion == 9:
    nota = 'A'
elif calificacion == 8:
    nota = 'B'
elif calificacion == 7:
    nota = 'C'
elif 0 <= calificacion <= 6:
    nota = 'F'
else:
    nota = 'Calificación no valida'

print(nota)
