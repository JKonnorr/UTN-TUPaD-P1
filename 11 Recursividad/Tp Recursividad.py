# TP Recursividad

#1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingresa un número: "))

for i in range(1, numero + 1):
        print(f"Factorial de {i}: {factorial(i)}")


#2
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingresa la posición hasta la que deseas generar la serie de Fibonacci: "))

print(f"Serie de Fibonacci hasta la posición {posicion}:")

for i in range(posicion + 1):
        print(f"Posición {i}: {fibonacci(i)}")


#3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = float(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a: {resultado}")


#4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingresa un número: "))
binario = decimal_a_binario(numero)

print(f"El número {numero} en binario es: {binario}")


#5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingresa una palabra para verificar si es palíndromo: ")
palindromo = es_palindromo(palabra)

if palindromo:
    print(f"{palabra} SI es palíndromo")
else:
    print(f"{palabra} NO es palíndromo")


#6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    
numero = int(input("Ingrese el número: "))
suma = suma_digitos(numero)

print(f"La suma de los Dígitos del número {numero} es {suma}")


#7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

bloques = int(input("Ingrese la cantidad de bloques que desea en la base de la pirámide: "))
cantidad_necesaria = contar_bloques(bloques)

print(f"Teniendo una base de {bloques} bloques, la cantidad de bloques total necesaria es {cantidad_necesaria}.")


#8
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo_digito = numero % 10
        resto = numero // 10
        return (1 if ultimo_digito == digito else 0) + contar_digito(resto, digito)

numero = int(input("Ingrese el número donde se va a buscar el dígito: "))
digito = int(input("Ingrese el dígito a buscar: "))
cantidad_encontrada = contar_digito(numero,digito)

print(f"La cantidad de veces que figura el digito {digito} en el número {numero} es: {cantidad_encontrada}")