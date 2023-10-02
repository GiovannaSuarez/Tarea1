# AHORCADO
import AHORCADO_Funciones
import random


username=str(input("Ingrese su nombre: ")).title()
words=["programacion","estres","lenguajes","python","java","datos"]
tries = 5
word = random.choice(words)
hidden_word = "_" * len(word)
used_words = ""
print(f"Bienvenido, {username}! La palabra del día de hoy tiene {len(word)} letras.")

while tries>0:
    print(hidden_word)
    letter = input("Ingrese una letra: ").lower()
    if len(letter)!=1 or letter.isalpha==False:
        print("Error. Solo puede ingresar letras y de una a la vez.")
    elif used_words.find(letter)==-1:
        checker = word.find(letter)
        if checker!=-1:
            hidden_word = AHORCADO_Funciones.check_word(letter,word,hidden_word)
            used_words = AHORCADO_Funciones.already_used(used_words, letter)
            if hidden_word.find("_")==-1:
                break
            else:
                continue
        else:
            tries = tries - 1
            print(f"Esta letra no se encuentra en la palabra. Intentos restantes: {tries}.")
            used_words = AHORCADO_Funciones.already_used(used_words, letter)
            continue
    else:
        print("Esta letra ya ha sido utilizada. Elija otra")
        continue
if tries > 0:
    print(f"¡Enhorabuena! Ha adivinado la palabra '{word}' con {tries} intentos restantes.")
else:
    print(f"¡Rayos! Se ha quedado sin intentos. La palabra secreta era '{word}'. ¡Mejor suerte para la próxima!")