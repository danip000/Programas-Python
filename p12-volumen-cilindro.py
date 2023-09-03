"""
Se desea calcular el volumen de un cilindro dado su radio y altura, usando la siguiente formula
Volumen = PI * (Radio * Radio) * Altura
"""

print('Calculo del volumen de un cilindro dado su radio y altura\n')
print('Ingresa los valores del radio y la altura separados por un enter\n')

radio , altura = int(input()) , int(input())

import math
volumen = math.pi * (radio * radio) * altura

print(f'\nCon los datos ingresados, el volumen del cilindro es de {volumen}')