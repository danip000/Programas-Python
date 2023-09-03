#Se desea calcular la hipotenusa de un triangulo rectangulo dadas las longitudes de sus lados, usando la siguiente formula

print('Calculo de la hipotenusa de un triangulo rectangulo\n')
print('Dame la longitud de los lados separados por un enter')

longlado1 , longlado2 = int(input()) , int(input())

import math

hipotenusa = math.sqrt (longlado1 * longlado1 + longlado2 * longlado2)

print(f'La hipotenusa para un triangulo rectangulo, cuyo valor del primer lado es {longlado1} y del segundo {longlado2}, es de {hipotenusa}')
