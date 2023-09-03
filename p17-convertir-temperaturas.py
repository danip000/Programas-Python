# Convierte grados celsius a grados Farenheit y viceversa

print('Convierte grados celsius a grados Farenheit y viceversa')

opcion = input('[C]entigrados a Farenheit\n[F]arenheit a centigrados\nElige ? ')
opcion = str.upper(opcion)

#Se puede agregar el str.upper en la misma linea 5 (colocandolo al inicio)

if opcion == 'C' :
    print('\nConviertiendo de Farenheit a centigrados')
    temp = float(input('Grados Farenheit ?'))
    res = (temp - 32) * 5 / 9
    print(f'{temp} grados farenheit equivalen a {res} grados centigrados')
else:
    print('\nConvirtiendo de centigrados a Frenheit')
    temp = float(input('Grados centigrados ? '))
    res = (temp * 9 / 5) + 32
    print(f'{temp} grados centigrados equivale a {res:.2f} grados Farenheit')
    
print('\nProceso terminado ...')
