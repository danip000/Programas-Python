#Dado el año de nacimiento, la suma de sus digitos individuales es el numero de la suerte. Mostrar los digitos individuales y el numero de la suerte

print('Numero de la suerte\nEl numero de la suerte se determina al sumar los digitos indivuales del año de nacimiento de una persona')
anionacimiento = input("Ingresa tu año de nacimiento : ")

# Validar que sea un número entero
if anionacimiento.isdigit():
    anionacimiento = int(anionacimiento)
    
    suma = sum(map(int, str(anionacimiento)))

    print(f'Número de la suerte: {suma}')
else:
    print("Ingresa un año de nacimiento válido.")
