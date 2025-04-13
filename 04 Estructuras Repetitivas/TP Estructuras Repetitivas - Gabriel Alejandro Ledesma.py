#TP

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(1, 101, 1):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero_entero = int(input("Ingrese un número entero: "))

if numero_entero == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0
    while numero_entero > 0:
        numero_entero //= 10
        cantidad_digitos += 1

print(f"La cantidad de digitos del número ingresado es {cantidad_digitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
acumulador = 0

for i in range(numero1+1, numero2, 1):
    acumulador += i
print(f"La suma de los números comprendidos entre {numero1} y {numero2} es {acumulador}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero_ingresado = int(input("Ingrese un número entero para empezar a sumar: "))
acumulador = 0

while numero_ingresado != 0:
    acumulador += numero_ingresado
    numero_ingresado = int(input("Ingrese otro número entero para sumar o ingrese 0 para finalizar: "))
print(f"La suma de todos los números ingresados es: {acumulador}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_aleatorio = random.randint(0, 9)
numero_ingresado = int(input("Adivine un número aleatorio entre 0 y 9: "))
contador = 1

while numero_ingresado != numero_aleatorio:
    contador += 1
    numero_ingresado = int(input("Incorrecto. Intente nuevamente: "))
print(f"Correcto! Tu cantidad de intentos fue: {contador}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero_ingresado = int(input("Ingrese un número entero: "))
acumulador = 0

for i in range(0, numero_ingresado, 1):
    acumulador += i
print(f"La suma de los números comprendidos entre 0 y {numero_ingresado} es: {acumulador}.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contador_positivos = 0
contador_negativos = 0
contador_pares = 0
contador_impares = 0

for i in range(1, 101, 1):
    numero_ingresado = int(input("Ingrese un número: "))
    if numero_ingresado % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    if numero_ingresado > 0:
        contador_positivos += 1
    else:
        contador_negativos += 1
print(f"La cantidad de números positivos es: {contador_positivos}")
print(f"La cantidad de números negativos es: {contador_negativos}")
print(f"La cantidad de números pares es: {contador_pares}")
print(f"La cantidad de números impares es: {contador_impares}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

acumulador = 0
for i in range(1, 101, 1):
    numero_ingresado = int(input("Ingrese un número: "))
    acumulador += numero_ingresado
    media = acumulador / 10
print (f"La media de los números ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_ingresado = input("Ingrese un número: ")
numero_invertido = numero_ingresado[::-1]
print(f"El número ingresado invertido es: {numero_invertido}.")