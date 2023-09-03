#Dados dos angulos de un triangulo, calcular el 3er angulo, usando la siguiente formula

print('Calculo del tercer angulo de un triangulo\n')
print('Dame dos angulos separados por un enter, para calcular el valor del tercero\n')

angulo1 , angulo2 = float(input()) , float(input())

angulo3 = 180 - (angulo1 + angulo2)

print(f'\nEl valor del tercer angulo dados los valores ingresados, es de {angulo3}')