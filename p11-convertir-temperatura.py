#Dada una temperatura en grados Celsius, obtener su equivalente en grados Farenheit, usando la siguiente formula:

print('Conversion de temperatura de grados Celsius a Farenheit\n')
print('Ingresa la temperatura en Celsius que quieras convertir\n')
celsius = int(input())

farenheit = (celsius * 9/5) + 32

print(f'\nLa temperatura de {celsius} grados Celsius, equivale a {farenheit} grados Farenheit')