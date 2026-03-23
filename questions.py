import random

words = {
    'tipos de datos': [
        "variable",
        "cadena",
        "entero",
        "lista"
    ],
    'programa': [
        "programa",
        "python",
        "funcion",
        "bucle",
    ]
}

def show_options(words):
    for name, item in words.items():
        print(f' - {name}')

guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()

show_options(words)
while True:
    category = input('Elegí una categoría: ')
    print()
    if type(category) == type(str()) and category in words.keys():
        word = random.choice(words[category])
        break
    else: 
        print('Ingresá una categoría existente.')

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        print("¡+6 puntos!")
        # Mostramos la puntuación final del jugador
        user = input('¡Ingresá 4 letras para registrarte!\n')
        points = attempts + 6
        print(f'¡{user[:4].upper()}: Tu puntaje fue de {points} de 12!')
        break
    
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    # Verificar si el caracter es correcto
    while True:
        letter = input("Ingresá una letra: ")
        # Verificar que el caracter ingresado sea una letra y sea solo un caracter
        if letter.isalpha() and len(letter) == 1:
            break
        else:
            print("Entrada no válida.")
    
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
        print("¡-1 punto!")
        
    print()
    
else:
    print(f"¡Perdiste! La palabra era: {word}")
    print(f"Tu puntaje es 0...")