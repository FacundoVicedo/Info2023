nombre = str(input("Por favor, ingrese su nombre: "))
numero = int(
    input(
        f"Bienvenid@, {nombre}. Por favor, ingrese un numero del 1 al 100, y si lo adivina ganará un premio. Tiene 8 intentos para adivinarlo: "
    )
)

import random

numero_ganador = random.randint(1, 100)
intentos = 7
print(numero_ganador)


for i in range(1, 8):
    if numero < numero_ganador:
        print(f"PISTA_____El numero ganador es mayor a {numero}_____")

    if numero > numero_ganador:
        print(f"PISTA_____El numero ganador es menor a {numero}_____")

    if numero != numero_ganador:
        numero = int(
            input(f"Por favor ingrese otro numero, le quedan {intentos} intentos: ")
        )
        intentos -= 1

        if intentos == 0:
            print(
                f"Usted se ha quedado sin intentos.\nEl numero que debía adivinar era el ·{numero_ganador}·"
            )

        if numero == numero_ganador:
            print(
                f"Felicidades, es usted el ganador del premio. Lo logró en el intento numero {intentos + 1}"
            )
