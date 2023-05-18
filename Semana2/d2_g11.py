frase = input('ingrese una frase:').lower().strip()
letra1 = input ('Ingrese una letra:').lower()
letra2 = input ('Ingrese una letra:').lower()
letra3 = input ('Ingrese la ultima letra:').lower()

count_letra1 = frase.count(letra1)
count_letra2 = frase.count(letra2)
count_letra3 = frase.count(letra3)

count_palabras = len(frase.split(" "))
primera_letra = frase[0]
ultima_letra = frase[-1]
texto_inverso = frase [::-1]
texto_orden_inverso = frase.split(" ")[::-1]
texto_orden_inverso2= " ".join (texto_orden_inverso)

print("el numero de veces que tu letra aparece en la frase es: ","\n", letra1,"=", count_letra1,"\n", letra2,"=", count_letra2,"\n", letra3,"=", count_letra3)
print("En el texto hay un total de: ",count_palabras,"palabras")
print("la primera letra de la frase es:",primera_letra,"y la ultima es",ultima_letra)
print("su texto en forma inversa es:",texto_inverso)
print (texto_orden_inverso2)

if "python" in frase:
    print("la palabra python se encuentra en la frase")
else:
    print ("la pabla python no se encuntra en la frase")

#-----GRUPO 11----------------
# Los integrantes del grupo son: 
# Joel Chavez, 
# Renzo Arrieta, 
# Pablo Acevedo, 
# Serial Trachta Matías Gastón, 
# Lugo Mauro Rodrigo, 
# Julio R. Escanciano Gonzalez, 
# Facundo Vicedo, 
# Gabriel Leiva, 
# Maximiliano Imanol Aguer, 
# Salto Cristian J.
#------------------------------