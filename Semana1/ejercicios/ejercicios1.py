# Escribe un programa que solicite al usuario su nombre y lo imprima en la pantalla

#nombre = input("¿Cual es su nombre?: ")
#print (nombre)

# 2-Escribe un programa que solicite al usuario su nombre y luego imprima un mensaje de bienvenida.

#nombre = input("¿Cual es su nombre?: ")
#print (f"Bienvenido {nombre}")

# 3-Crea un programa que pida al usuario su edad y lo imprima en pantalla.

#edad = input("Cual es su edad: ")
#print ("Su edad es " + edad)

# 4-Crea un programa que calcule la suma de dos números y lo imprima en pantalla.

#print("Para sumar dos numeros, ingrese el primero y debajo el otro")
#suma = input("el primero: ")
#suma2 = input("y el segundo: ")
#print(f"El resultado es: {int(suma) + int(suma2)}")

# 5-Crea un programa que pida al usuario dos números enteros y muestre en pantalla su cociente y su resto.

#numero1 = int(input("escriba un numero: "))
#numero2 = int(input("escriba el segundo: "))
#cociente = int(numero1/numero2)
#resto = numero1 % numero2
#print(f"El cociente es: {cociente} y el resto es: {resto}")

# 11-Crea un programa que pida al usuario una palabra y muestre en pantalla cuántas letras tiene.

#palabra = input("escriba una palabra: ")
#print(f"Su palabra tiene {len(palabra)} letras")

# 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
#dd/mm/aaaa y luego imprima su edad en años.

#AnoActual= input("En que año estamos?: ")
#FechaNacimiento= input("cual es su fecha de nacimiento? Escribalo en formato dd/mm/aaaa: ")
#dia, mes, anio = FechaNacimiento.split("/")
#edad = int(AnoActual) - int(anio)
#print(f"Usted tiene {edad} años")

# 13-Escribe un programa que solicite al usuario su nombre y su edad, y luego imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

#nombre = input("Por favor coloque su nombre: ")
#edad= input("Por favor coloque su edad: ")
#print(f"{nombre}, usted tendrá {int(edad) + 10} años, dentro de 10 años")

# 14-Escribe un programa que solicite al usuario un número entero y luego imprima el doble y el triple de ese número.

#numero= input("Coloque un numero: ")
#print(f"El doble es: {int(numero)*2} y el triple es: {int(numero)*3}")

# 15-Escribe un programa que solicite al usuario una temperatura en grados Celsius y luego imprima la temperatura equivalente en grados Fahrenheit. La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

#temperatura = input("Coloque una temperatrura en grados celcius: ")
#print(f"La temperatura en grados Fahrenheit es: {int(int(temperatura)*1.8 + 32)} ")

# 16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule e imprima su índice de masa corporal (IMC). La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

#peso=int(input("Escriba su peso en kg: "))
#altura=float(input("Escriba su altura en metros: "))
#print(f"Su IMC es de {peso / altura ** 2}")

# 17-Escribe un programa que solicite al usuario dos palabras y luego las imprima en orden inverso. 
#  Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir "mundo hola". Importante!!! Utiliza un solo print()

#PrimerPalabra = input("Escriba una palabra: ")
#SegundaPalabra = input("Escriba segunda palabra: ")
#print(SegundaPalabra + " " + PrimerPalabra)

# 19-Escribe un programa que solicite al usuario un número decimal y luego imprima la parte entera y decimal por separado.

#numero= input("Coliuqe un numero decimal: ")
#entero, decimal= numero.split(".")
#print(f"El numero entero es: {entero} y el decimal es: {decimal}")

#------------------------------Desafío 1:
#Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
#sus ventas totales y el departamento comercial te solicita que ayudes a los
#vendedores a calcular sus comisiones creando un programa que les pregunte su
#nombre y cuánto han vendido en éste mes.
#Tu programa le va a responder con una frase que incluya su nombre y el monto
#que le corresponde por las comisiones

#nombre=input("Colouqe su nombre: ")
#ventas= float(input("Cuanto ha vendido en pesos este mes?: "))
#print(f"Bienvenido {nombre}, con respecto a la cantidad de ventas hechas este mes, usted tiene una comisión de: ${int(ventas) * 0.06}")

#------------------------------Desafío 2:
#Escribe un programa que solicite al usuario su información personal, incluyendo
#su nombre completo, edad, estatura, peso, dirección y número de teléfono.
#A continuación, el programa deberá imprimir un mensaje con los datos
#ingresados por el usuario en el siguiente formato:
#La información ingresada es la siguiente:
#Nombre completo: [nombre completo]
#Edad: [edad]
#Estatura: [estatura] cm
#Peso: [peso] kg
#Dirección: [dirección]
#Número de teléfono: [número de teléfono]

#datos= input("Porfavor coloque su nombre completo, su edad, estatura en centimetros, su peso en kg, dirección y numero telefonico; separados por una coma: ")
#nombre, edad, estatura, peso, direccion, numero = datos.split(",")
#print(f"Nombre completo: {nombre}\nEdad: {edad}\nEstatura: {estatura} cm\nPeso: {peso} kg\nDirección: {direccion}\nNúmero de telefono: {numero} ")

