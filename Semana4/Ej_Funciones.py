# 1-Crea una función llamada suma que tome dos números como parámetros y devuelva la suma de ellos.
"""
def suma(a,b):
    return a + b

print(suma(2,3))
"""

# 2-Crea una función llamada saludo que tome el nombre de una persona como parámetro e imprima un saludo personalizado.
"""
def saludo(nombre):
    print("Hola,", nombre)

saludo("Facundo")
"""

# 3-Crea una función llamada invertir_cadena que tome una cadena de texto como parámetro y devuelva la cadena invertida.
"""
def invertir_cadena(cadena):
    return cadena[::-1]

print(invertir_cadena("Hola que pedo wey"))
"""

# 4-Crea una función llamada es_capicua que tome un número como parámetro y devuelva True si es capicúa (es decir, 
# si se lee igual de izquierda a derecha que de derecha a izquierda) y False en caso contrario.
"""
def es_capicua(numero):
    numero = str(numero)
    return numero == numero[::-1]
print(es_capicua(2442))
print(es_capicua(1234))
"""

# 5-Crea una función llamada es_divisible que tome dos números enteros como parámetros y 
# devuelva Es divisible si el primer número es divisible por el segundo número, o No es divisible en caso contrario
"""
def es_divisible(n1,n2):
    if n1 % n2 == 0:
        return "Es divisible"
    else:
        return "No es divisible"

print(es_divisible(23,2))
print(es_divisible(20,2))
"""

# 6-Crea una función llamada es_par que tome un número como parámetro y devuelva Es par 
# si el numero cumple con dichas condiciones y en caso contrario devuelva Es impar o No es par.
"""
def es_par(numero):
    if numero % 2 == 0:
        return "Es par"
    else:
        return "Es impar"
print(es_par(23))
print(es_par(10))
"""

# 7-Crea una función llamada imprimir_pares que tome un número entero como parámetro e 
# imprima todos los números pares desde 1 hasta ese número.
"""
def imprimir_pares(numero):
    for pares in range(2, numero+1, 2):
        print(pares)

imprimir_pares(20)
"""

# 8-Crea una función llamada es_palindromo que tome una cadena de texto como parámetro y 
# devuelva es palindromo si es un palíndromo (es decir, si se lee igual de izquierda a derecha 
# que de derecha a izquierda) y no es palindromo en caso contrario.
"""
def es_palindromo(cadena):
    if cadena.lower() == cadena[::-1].lower():
        return "Es palindromo"
    else:
        return "No es palindromo"

print(es_palindromo("ojo"))
print(es_palindromo("marsupial"))
"""

# 9-Crea una función llamada promedio que tome una lista de números como parámetro y devuelva el promedio de esos números.
"""
def promedio(lista):
    return sum(lista) / len(lista)

print(promedio([4,5,4]))
"""

# 10-Crea una función llamada calcular_factorial que tome un número entero como parámetro y devuelva el factorial de ese número. 
# El factorial de un número entero positivo n se define como el producto de todos los números enteros positivos desde 1 hasta n.
"""
def calcular_factorial(numero):
    producto = 1
    for n in range(1, numero+1):
        producto *= n
        print(producto)
    return producto

print(calcular_factorial(5))
"""

# 11-Crea una función llamada contar_vocales que tome una cadena de texto como parámetro y devuelva el número de vocales que contiene.
"""
def contar_vocales(cadena):
    vocales = 0
    for letra in cadena:
        if letra in "aeiouAEIOU":
            vocales += 1
    return vocales
    
print(contar_vocales("Hola yO soy facUndo"))
"""

# 12-Crea una función llamada convertir_temperatura que tome una temperatura en grados Celsius y la convierta a grados Fahrenheit. 
# La fórmula de conversión es: Fahrenheit = (Celsius * 9/5) + 32.
"""
def convertir_temperatura(temperatura_celsius):
    return (temperatura_celsius * 1.8) + 32

print(convertir_temperatura(159))
"""

# 13-Crea una función llamada calcular_descuento que tome dos parámetros: precio y porcentaje_descuento. 
# La función debe calcular y devolver el precio después de aplicar el descuento.
"""
def calcular_descuento(precio, porcentaje_descuento):
    descuento = porcentaje_descuento / 100
    descuento_total = precio * descuento
    precio_con_descuento = precio - descuento_total
    return precio_con_descuento

print(calcular_descuento(200,1))
"""

# 14-Crea una función llamada encontrar_maximo que tome una lista de números como parámetro y devuelva el número máximo de la lista.
"""
def encontrar_maximo(lista_numeros):
    return max(lista_numeros)

print(encontrar_maximo([1,2,3,400,5,65]))
"""

# 15-Crea una función llamada contar_palabras que tome una cadena de texto como parámetro y devuelva el número de palabras que contiene. 
# Se considera que las palabras están separadas por espacios.
"""
def contar_palabras(cadena):
    palabras = cadena.split(" ")
    return len(palabras)

print(contar_palabras("Hola mi amor, estas programando solo enserio?"))
"""

# 16-Crea una función llamada eliminar_duplicados que tome una lista como parámetro y devuelva una nueva lista sin duplicados, conservando el orden original.
"""
def eliminar_duplicados(lista):
    nueva_lista = []
    
    for elemento in lista:
        if not elemento in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista

print(eliminar_duplicados(["hola","besos", 1, 1, 3, 3, 2, "hola", "besos",2]))
"""

# 17-Crea una función llamada es_anagrama que tome dos cadenas de texto como parámetros y devuelva True si son anagramas
# (es decir, si tienen las mismas letras pero en distinto orden), o False en caso contrario.
"""
def es_anagrama(cad1, cad2):
    # convertimos cada cadena en minusculas
    cad1 = cad1.lower()
    cad2 = cad2.lower()

    # convertimos las cadenas a listas
    lista_cad1 = list(cad1)
    lista_cad2 = list(cad2)

    # ordenamos ambas listas
    lista_cad1.sort()
    lista_cad2.sort()

    # unimos, los caracteres de cada lista, convirtiendolo otra vez a una cadena
    cad1_ordenada = "".join(lista_cad1)
    cad2_ordenada = "".join(lista_cad2)

    # comprobamos si la cadena 1 es igual a la cadena 2
    return cad1_ordenada == cad2_ordenada

print(es_anagrama("hola todo bien oasdasd que onda", "todo piola mi negro"))
print(es_anagrama("esto deberia ser un anagrama", "est o   deberiA ser un anagrama"))
print(es_anagrama("hOla", "alho"))
"""

# 18-Crea una función llamada calcular_mayor_diferencia que tome una lista de números como parámetro y devuelva la mayor
#  diferencia entre el numero mas alto y el numero mas bajo en la lista.
"""
def calcular_mayor_diferencia(lista_numeros):
    return max(lista_numeros) - min(lista_numeros)

print(calcular_mayor_diferencia([1,2,3,4,5,20]))
"""

# 19-Crea una función llamada es_bisiesto que tome un año como parámetro y devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario.
# Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.
"""
def es_bisiesto(año):
    if año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
        return "Es año bisiesto"
    elif año % 4 == 0 and not año % 100 == 0:
        return "Es año bisiesto"
    else:
        return "No es año bisiesto"

print(es_bisiesto(2020))
print(es_bisiesto(2024))
print(es_bisiesto(2023))
print(es_bisiesto(2000))
"""