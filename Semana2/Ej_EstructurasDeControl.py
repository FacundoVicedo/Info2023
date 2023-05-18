# 1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es mayor de edad (18 años o más) o no.

#edad=int(input("Cual es su edad?: "))

#if edad >= 18:
#    print("usted es mayor de edad.")
#if edad < 18:
#    print("Usted es menor de edad.")

#2-Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es positivo, negativo o cero.

#numero= int(input("Escriba un numero entero: "))
#if numero > 0:
#    print("el numero es positivo")
#elif numero == 0:
#    print("el numero es cero")
#else:
#    print("el numero es negativo")

#3-Escribir un programa que pida al usuario dos números y muestre por pantalla cuál de ellos es mayor.

#numeros= input("Escriba 2 numeros: ")
#numero1, numero2 = numeros.split(" ")

#if numero1 > numero2:
#    print(f"{numero1} es mayor")
#elif numero2 > numero1:
#    print(f"{numero2} es mayor")
#else:
#    print(numero1)

#4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla si está aprobado (5 o más) o no.

#nota = int(input("Escriba una nota de calificación del 0 al 10: "))
#if nota >= 5:
#    print("Está aprobado :D")
#else:
#    print("No aprobó :(")

#5-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar

#numero=int(input("Escriba un numero entero: "))
#if numero%2 == 0:
#    print("es par")
#else:
#    print("Es impar")

# 6-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es múltiplo de 2 y de 3 a la vez.

#numero= int(input("Escriba un numero entero: "))
#if numero%2 == 0 and numero%3 == 0:
#    print("Este numero es multiplo de 2 y 3.")
#else:
#    print("Este numero no es multiplo de 2 o 3.")    

#7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
#es una letra mayúscula, una letra minúscula, un número o un carácter especial.

#caracter= input("Escriba un caractér cualquiera: ")

#if caracter >="0" and caracter <="9":
#    print("El caractér es un numero")
#elif caracter >= "a" and caracter <= "z":
#    print("Es letra minuscula")
#elif caracter >= "A" and caracter <="Z":
#    print("es mayuscula")
#else:
#    print("es caracter especial")

   #################################   SINO TAMBIEN SE PUEDE DE LA SIGUIENTE MANERA   ######################################

#caracter = input("Ingresa un caracter: ")
#if caracter.isupper(): #pregunta si es mayuscula
#    print("El caracter es una letra mayuscula")
#elif caracter.islower(): #pregunta si es minuscula
#    print("El caracter es una letra minuscula")
#elif caracter.isdigit(): #pregunta si es un digito
#    print("El caracter es un numero")
#else:
#    print("El caracter es especial")


  # 8-Escribir un programa que pida al usuario una cadena de caracteres y muestre por pantalla si contiene la letra "a"

#cadena = input("Escriba una cadena de caracteres: ")


# 9-Escribir un programa que pida al usuario tres números y muestre por pantalla el mayor de ellos.
#numeros= input("Escriba 3 numeros diferentes: ")
#numero1, numero2, numero3 = numeros.split(" ")

#if numero1 > numero2 and numero1 > numero3:
#    print(f"{numero1} es mayor.")
#elif numero2 > numero1 and numero2 > numero3:
#    print(f"{numero2} es mayor.")
#else:
#    print(f"{numero3} es mayor.")

# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es una vocal o una consonante.
#letra = input("Escriba una letra: ")
#if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#    print("su letra es una vocal")
#else:
#    print("Su letra en una consonante.")

# 11-Escribir un programa que pida al usuario dos números y muestre por pantalla la suma de ellos solo si ambos son pares.

#numeros= input("Escriba 2 numeros: ")
#numero1, numero2= numeros.split(" ")

#if int(numero1) % 2 == 0 and int(numero2) % 2 == 0:
#    print(int(numero1) + int(numero2))
#else:
#    print("Sus numeros no son pares")


