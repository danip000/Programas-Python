#Lee datos y envia un saludo
print('hola mundo')
print("Leyendo datos y enviando un saludo \n")
nombre = input("Dame tu nombre : ")
edad = int(input("Dame la edad : "))
peso = float(input("Dame tu peso : "))
print(f"\nTu nombre es {nombre} bienvenido a Python, tu edad es {edad}, tu peso es {peso}")
print(type(nombre))
print(type(edad))
print(type(peso))

#Calcular el area de un circulo
import math
print("Calculando el area de un circulo \n")
print("Dame el radio : ")
radio = float(input())
area = math.pi*radio**2
print(f"\nEl circulo de radio {radio}, tiene un area de {area}")

#Calcular el area de un triangulo
print("Calculando el area de un triangulo\n")
print("Dame la base y la altura se parados por un enter")
base, altura = int(input()), int(input())
area = base * altura / 2
print(f"El triangulo de base {base} y altura {altura} tiene un area de {area}")

#Calcular la paga total de un trabajador
print("Calculando la paga de un trabajador\n")
print("Nombre : ")
nombre = input()
print("Horas trabajadas : ")
horas = int(input())
print("Paga por hora : ")
paga = float(input())
tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto
print("Resumen de pagos: \n")
print(f"El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga} pesos por hora, impuesto de {tasa}%")
print(f"Paga bruta {pagabruta}")
print(f"Impuesto {impuesto}")
print(f"Paga neta {paganeta}")
