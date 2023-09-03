"""
Dada una cantidad en horas, calcular su equivalente en dias, minutos y segundos, considerando que:

1 dia tiene 24 horas
1 hora tiene 60 minutos
1 minuto tiene 60 segundos
"""

print('Convertir las horas en su equivalente en dias, minutos y segundos')

horas = int(input('Ingresa las horas que quieras transformar :'))

dias = (horas / 24)
minutos = (horas * 60)
segundos = (minutos * 60)

print(f'{horas} horas ingresadas equivalen a :\n{dias} dias\n{minutos} minutos\n{segundos} segundos')