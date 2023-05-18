# 1-Escribe un programa que pida al usuario una palabra y luego imprima cada letra de la palabra en una línea separada.
"""
palabra = input("Escribi una palabra: ")

for separar in palabra:
    print(separar)
"""

# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos los números naturales del 1 hasta ese número.
"""
numero = int(input("Ingrese un número: "))
i = 1
suma = 0

while i <= numero:
    suma += i
    i += 1

print(f"suma es: {suma}")
"""

# 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de multiplicar correspondiente a ese número del 1 al 10.
"""
numero = int(input("ingrese un numero: "))

i = 1

while i < 11:
    print(i * numero)
    i += 1
"""
# 4-Escribe un programa que imprima los números pares del 1 al 100.
"""
i = 1

while i < 101:
    if i % 2 == 0:
        print(i)
    i += 1
"""

# 5-Escribe un programa que imprima la suma de todos los números pares del 1 al 100. 
"""
i = 1
suma = 0

while i < 101:
    if i % 2 == 0:
        suma += i
    i += 1
print ("la suma de los numeros pares es: ", suma)
"""

# 6-Escribe un programa que pida al usuario una palabra y luego imprima la misma palabra pero con las letras en orden inverso.
"""
palabra= input("Escriba una palabra: ")
revertido = palabra[::-1]
for letra in revertido:
    print(letra)
"""

# 7-Escribe un programa que pida al usuario una palabra y determine si es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).
"""
palabra1 = input("escribi una palabra: ")
palabra2 = palabra1[::-1]

while palabra1 != palabra2:
    print("Su palabra NO es un palindromo")
    palabra1 = input("Ingrese otra palabra: ")
    palabra2 = palabra1[::-1]
else:
    print("Su palabra SI es un palindromo")
"""

# 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima el número de palabras que contiene.
"""
frase = input("escriba una frase: ")

cont = 0

for i in frase.split(" "):
    cont += 1

print(cont)
"""

# 9-Escribe un programa que pida al usuario un número y luego imprima la secuencia de Fibonacci correspondiente a ese número
"""
numero = int(input("ingrese un numero: "))
a = 0
b = 1
suma = a + b

while suma <= numero:
    print(suma)
    a = b
    b = suma
    suma = a + b
"""

# 10-Escribe un programa que pida al usuario una cadena de texto y luego imprima la misma cadena pero con todas las vocales en mayúscula.
"""
frase = input("ingrese una frase: ")
frase_midificada = ""

for letra in frase:
    if letra in "aeiouAEIOU":
        frase_midificada += letra.upper()

    else:
        frase_midificada += letra

print(frase_midificada)
"""        

# 11-Escribe un programa que pida al usuario un número y calcule su factorial. Un factorial es el producto que resulta de multiplicar un número entero positivo
# dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial de 4 es 4! = 4 × 3 × 2 × 1 = 24.
"""
numero = int(input("Ingrese un numero entero: "))

resultado = 1

for i in range(1 , numero+1):
        resultado = i * resultado

print(resultado)
"""

# 12-Escribe un programa que pida al usuario una lista de números separados por comas y calcule su promedio.
"""
numeros = input("escriba una lista de numeros separados por comas: ")
lista = numeros.split(",")

suma = 0
for i in lista:
    if i.isdigit():
        suma += int(i)
print(suma)

print("El promedio es: ", suma/len(lista))
"""


# 13-Escribe un programa que pida al usuario un número y luego imprima un triángulo de asteriscos con esa cantidad de filas.
"""
asteriscos = int(input("Ingrese un numero: "))

for i in range(1, asteriscos+1):
    print(i * "*")
"""

# 14-Escribe un programa que pida al usuario un número y luego imprima un triángulo de números como el siguiente:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
"""
numeros = int(input("ingrese un numero: "))

for i in range(1, numeros+1):
    print(str(f"{i} ")*i)
"""

# 15-Escribe un programa que pida al usuario una cadena de texto y determine cuántas veces aparece cada letra en la cadena
"""
frase = input("ingrese una frase: ").replace(" ", "")


for letra in frase:
    print("la letra", letra, "se imprime", frase.count(letra), "veces.")
"""
    
# 16-Escribe un programa que pida al usuario una cadena de texto y luego imprima la misma cadena pero con cada palabra al revés
"""
frase = input("ingrese una frase: ")
atras = frase[::-1]

for palabra in atras.split(" "):
    print(palabra)
"""

# 18-Escribe un programa que pida al usuario un número y luego imprima un triángulo de números como el siguiente:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
"""
numero = int(input("Ingresar numero: "))

triangulo = ""
count1 = 1  # salto de linea cuando es == n
count2 = 0  # contador de saltos de linea

for n in range(1, numero+1):
    triangulo += str(n)+" "
    if count1 == n:
        triangulo += "\n"
        count2 += 1
        count1 += count2+1

print(triangulo)
"""















