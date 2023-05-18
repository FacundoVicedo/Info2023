texto = input("Ingrese por favor un texto cualquiera, como por ejemplo un artículo o una frase: ")
letras = input("Ahora ingrese tres letras diferentes sin separarlas: ")


lista = list(texto.lower())
lista_letras = list(letras.lower())

print(f"la letra {lista_letras[0]} aparece {lista.count(lista_letras[0])} veces. \nLa letra {lista_letras[1]} aparece {lista.count(lista_letras[1])} veces. \nLa letra {lista_letras[2]} aparece {lista.count(lista_letras[2])} veces.")


lista_de_palabras = texto.lower().split(" ")
print(f"En todo el texto hay un total de {len(lista_de_palabras)} palabras.")


print(f"La primera letra es la: {lista[0]} \nLa última letra es la: {lista[-1]}")


texto_al_reves = texto [::-1]
print(texto_al_reves)


#python = "python" in lista_de_palabras
#mensaje = {
#    True : "La palabra python aparece en el texto.",
#    False : "La palabra python no aparece en el texto."
#}

#print(mensaje[python])

python = "python" in texto
mensaje = {
    True : "La palabra python aparece en el texto",
    False : "La palabra python no aparece en el texto"
}
print(mensaje[python])












