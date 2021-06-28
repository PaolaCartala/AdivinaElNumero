import random

print("Bienvenido al programa 'Adivina el número'!\n")
name = input("Ingresa tu nombre: \n")
print(f"Hola {name}!")

print("Instrucciones:\n El programa escoge un número al azar entre 1 y 100, y tenés 10 intentos para adivinarlo. Pero no te preocupes, te daremos pistas si el número es más alto o más bajo.\n Mientras menos intentos utilices para adivinar, mayor será tu puntaje. A jugar!\n")

# --- Variables ---
# -- Contador --
count = 0

# -- Puntaje --
puntaje = 10

# -- Número aleatorio --
aleatorio = random.randint(1, 100)

# -- Número elegido por el usuario --
num = None

# --- Principal ---
# -- Mientras el número no sea igual al aleatorio --
while num != aleatorio:
    if count < 10: # -- Si el contador es menor a 10 --
        num = int(input("Ingrese un número: \n"))
        if num > aleatorio: # -- Pista si el número elegido es mayor al aleatorio --
            print(f"El número {num} es mayor.")
        elif num < aleatorio: # -- Pista si el número elegido es menor al aleatorio --
            print(f"El número {num} es menor.")
        count += 1 # -- Luego del intento, incrementará en 1 el contador --
        puntaje -= 1 # -- Disminuirá el puntaje --
    else: # -- Si no tenemos más intentos --
        print("Te quedaste sin intentos!")

if num == aleatorio: # -- En caso de adivinar el número --
    print("Ganaste!")
    print(f"Puntaje: {puntaje} puntos.")