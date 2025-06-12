# TP Funciones

#1
def imprimir_hola_mundo():
    print("Hola Mundo!")

saludo = imprimir_hola_mundo()


#2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Por favor, ingresa tu nombre: ")

saludar_usuario(nombre)


#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

nombre = input("Ingrese su NOMRBE: ")
apellido = input("Ingrese su APELLIDO: ")
edad = input("Ingrese su EDAD: ")
residencia = input("Ingrese su LUGAR DE RESIDENCIA: ")

informacion_personal(nombre, apellido, edad, residencia)


#4
def calcular_area_circulo(radio):
   area = 3.14 * (radio ** 2)
   return area
 
def calcular_perimetro_circulo(radio):
   perimetro = 2 * 3.14 * radio
   return perimetro

radio = float(input("Ingrese por favor el Radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área es de: {area:.2f} y el perímetro es de: {perimetro:.2f}")


#5
def segundos_a_horas(segundos):
    horas = (segundos / 60) / 60
    return horas

segundos = int(input("Ingrese los segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} es equivalente a {horas:.2f}.")


#6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingrese un número para ver su tabla de multiplicación: "))

tabla_multiplicar(num)


#7
def operaciones_basicas(a,b):
    print(f"La SUMA es: {a+b}") 
    print(f"La RESTA es: {a-b}") 
    print(f"La MULTIPLICACION es: {a*b}") 
    print(f"La DIVISION es: {a/b:.2f}") 

print("A continuación, ingrese 2 números para mostrar sus operaciones basicas: ")
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

operaciones_basicas(a,b)


#8
def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese por favor su peso en KG: "))
altura = float(input("Ingrese su altura en Metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")
print("\nClasificación general (según la OMS):\n")
print("    Menor a 18.5 → Bajo peso")
print("    18.5 a 24.9 → Normal")
print("    25.0 a 29.9 → Sobrepeso")
print("    30.0 o más → Obesidad")


#9
def celsius_a_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

celcius = float(input("Ingrese la temperatura en celsius: "))
fahrenheit = celsius_a_fahrenheit(celcius)

print(f"La temperatura de {celcius}°C equivale a {fahrenheit:.2f}°F")


#10
def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    return promedio

print("A continuacion ingrese 3 números para obtener el promedio:")
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a,b,c)
print(f"El promedio de los 3 números ingresados es: {promedio:.2f}")