#Operaciones matematicas
"""
x = 10.5 se ponen valores para ver si funciona el programa
y = 2.5
"""

x = float(input('Dame el valor de x ?'))
y = float(input('Dame el valor de y ?'))

suma = x + y
resta = x - y
mul = x * y
res = x % y
exp = x ** y
div = x / y
dive = x // y
"""
print(f'Suma {suma}\nResta {resta}\nMultiplicacion {mul}\nResiduo {res}\n')
print(f'Exponienciacion {exp}\nDivision {div}\nDivision entera {dive}')
Esta es otra forma de guardar un comentario (#) y que no se muestre en la ejecucion del programa 
"""

print(f'Suma {suma}\nResta {resta}\nMultiplicacion {mul}\nResiduo {res}\n')
print(f'Exponienciacion {exp}\nDivision {div}\nDivision entera {dive}')

#Otra forma de hacerlo es haciendo print en cada operacion, de esta manera se pueden alinear de manera mas facil los digitos para su mejor comprension

#Un error de ejecucion muy frecuente en programacion es que no se puede dividir entre 0, se llama error en tiempo de ejecucion.