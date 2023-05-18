# 1-Crear un diccionario con los nombres de tres frutas y sus respectivos precios y mostrar el diccionario completo.

frutas={"Manzana": "$25", "Durazno":"$50", "Naranja":"$40"}
print(frutas)

#2-Crear una lista con los nombres de tres ciudades y agregar una cuarta ciudad al final de la lista.

ciudades= ["La Plata", "Resistencia", "Corrientes"]
print(ciudades)
ciudades.append("Rosario")
print(ciudades)

#3-Crear una lista con los nombres de tres países y mostrar el segundo país de la lista.

paises=["Argentina", "Francia", "Brasil"]
print(paises[1])

# 4-Crear un diccionario con los nombres de tres personas y sus respectivas edades. Mostrar la edad de la tercera persona en el diccionario.

personas={"Pedro":54, "Arturo":23, "Gonzalo":30}
print(personas["Gonzalo"])

# 5-Crear un set/conjunto con los números del 1 al 10 y mostrar el número más grande en el conjunto.

conjunto={1,2,3,4,5,6,8,10,9,7}
print (max(conjunto))

# 6-Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número de elementos en el conjunto.

conjunto_impar={1,3,5,7,9}
print(len(conjunto_impar))

# 7-Crear un diccionario con los nombres de tres ciudades y sus respectivas poblaciones.
# Agregar una cuarta ciudad al diccionario con su respectiva población. Mostrar el diccionario resultante.

poblaciones= {"Ciudad de Buenos Aires": "2.890.151", "Córdoba": "1.317.298", "Santa Fe": "948.312"}
print(poblaciones)
poblaciones["Tucumán"]="548.866"
print(poblaciones)

# 8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso.

inverso=[1,2,3,4,5,6,7,8,9,10]
inverso.reverse()
print(inverso)

# 9-Crear una lista con los nombres de tres países y ordenar la lista en orden alfabético. Mostrar la lista resultante.

paises_alfabeticos=["Resistencia", "Otawa", "Sidney"]
paises_alfabeticos.sort()
print(paises_alfabeticos)

# 10-Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la lista. Mostrar la lista resultante.

dos_frutas=["manzana", "naranja", "mandarina"]
del dos_frutas[1]
print(dos_frutas)

# 11-Crear una lista con los nombres de tres animales y agregar una cuarta animal al principio de la lista. Mostrar la lista resultante.

animales= ["jaguar", "elefante", "tigre"]
animales.insert(0, "ballena")
print(animales)

# 12-Crear una lista con los nombres de tres países y reemplazar el segundo país de la lista por otro país. Mostrar la lista resultante.

reemplazar= ["berlin", "tokio", "uruguay"]
reemplazar[1] = "argentina"
print(reemplazar)

# 13-Crear una lista con los nombres de tres colores y agregar dos colores más al final de la lista. Mostrar la lista resultante.

colores=["azul", "negro", "amarillo"]
colores.extend(["rojo", "rosa"])
print(colores)

# 14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los elementos de la tupla.

tupla=(1,2,3,4,5)
print(sum(tupla))