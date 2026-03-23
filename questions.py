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

category_randomized = []

#Muestra las opciones de categorías
def show_options(words):
    for name, item in words.items():
        print(f' - {name}')
        
# Pedir al jugador que elija una categoría de entre las opciones mostradas
def select_category(words):
    while True:
        category = input('Elegí una categoría: ')
        print()
        if type(category) == type(str()) and category in words.keys():
            category_randomized = random.sample(words[category],len(words[category]))
            break
        else: 
            print('Ingresá una categoría existente.')
    return category_randomized

print("¡Bienvenido al Ahorcado!")
print()

# Muestra las categorías
show_options(words)
# Pide seleccionar una
category_randomized = select_category(words)  
# Se posiciona en la primera palabra de category_randomized    
i = 0   
            
while True:
    
    guessed = []
    attempts = 6
            
    word = category_randomized[i]

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
        
    # Preguntar si el jugador quiere volver a jugar
    play_again = input(" ¿Volver a jugar? (SI/NO) ")
    while True:
        match play_again.upper():
            case 'SI':
                # Mientras queden opciones no vistas en category_randomized
                if i + 1 < len(category_randomized):
                    while True:
                        change_category = input("¿Cambiar categoría? (SI/NO) ")
                        print()
                        match change_category.upper():
                            case 'SI':
                                # Mostrar opciones de categorías y elegir una
                                show_options(words)
                                category_randomized = select_category(words)  
                                i = 0
                                break
                            case 'NO':
                                # Mostrar la siguiente palabra en category_randomized
                                i += 1
                                break
                            case _:
                                print('Por favor, ingresar "SI" o "NO".')
                # Si no quedan opciones no vistas en la categoría
                else:
                    show_options(words)
                    # Si se elige la misma categoría, se repetirán las palabras
                    category_randomized = select_category(words)  
                    i = 0   
                break
            case 'NO':
                print("Juego terminado.")
                break
            case _:
                print('Por favor, ingresar "SI" o "NO".')
    
    # Cortar el while True que engloba todo el juego
    if play_again.upper() == 'NO':
        break