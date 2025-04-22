# 1

lista1 = list(range(0,101,4))
print(lista1)

#2

plataformas_streaming = ["Netflix", "HBO MAX", "Disney+", "Apple TV", "Amazon Prime"]
print(plataformas_streaming[3])

#3

lista_vacia = []
lista_vacia.append("Televisor")
lista_vacia.append("Monitor")
lista_vacia.append("Proyector")
print(lista_vacia)

#4

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)

#5

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Este código elimina el número más grande de la lista numeros y luego imprime la lista resultante.

#6

lista6 = list(range(10,31,5))
print(lista6[0:2])

#7

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "voyage"
autos[2] = "fox"
print(autos)

#8

dobles = []
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)

#9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#10

lista_anidada = []
lista_anidada[0] = 15
lista_anidada[1] = True
lista_anidada[2][0] = 25.5
lista_anidada[2][1] = 57.9
lista_anidada[2][2] = 30.6
lista_anidada[3] = False
print(lista_anidada)
