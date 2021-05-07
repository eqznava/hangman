import os
import random

def limpiar():
    os.system('cls')


def read():
    words = []
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/data.txt', 'r', encoding = 'utf-8' ) as file:
        for line in file:
            words.append(line)
        random_word = random.choice(words)
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/random_word.txt','w', encoding = 'utf-8') as r_word:
        r_word.write(random_word)
        r_word.close()
        return random_word


def transform_to_list():
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/random_word.txt', 'r', encoding  = 'utf-8') as file:
        for line in file:
            word_to_list = line
            wtl = list(word_to_list)
            wtl.pop()
    return wtl


def transform_characters(lts=[]):
    all_index = []
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/rw_transform.txt','w', encoding='utf-8') as file:
        for i in range(len(lts)):
            all_index.append('_')
        for i in all_index:
            print(i, end = ' ')
        underscore = ''.join(all_index)
        file.write(underscore)
    

def com_lett(my_letter):
    word_to_list = []
    words = []
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/random_word.txt','r', encoding='utf-8') as file:
        for line in file:
            word_to_list = line
            wtl = list(word_to_list)
            wtl.pop()
    indices = [indice for indice, lett in enumerate(wtl) if lett == my_letter]
    found_letters = [letters for letters in wtl if letters == my_letter]
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/rw_transform.txt','r', encoding='utf-8') as file:
        for line in file:
            words = line
            w = list(words)
        for indexWTL in range(len(wtl)):
            for valueW in indices:
                if indexWTL == valueW:
                    w[valueW] = found_letters[0]
    update(w)


def update(w):
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/rw_transform.txt','w', encoding='utf-8') as file:
        a = ''.join(w)
        file.write(a)
        

def show_update():
    update_guess = []
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/rw_transform.txt', 'r', encoding='utf-8') as file:
        for line in file:
           update_guess = line
           sUl = list(update_guess)
        for lett in sUl:
            return str(lett) 
    
def main():    
    print(read())
    print('\n')
    transform_characters(transform_to_list())
    print('\n')
    my_letter = input('Try to guess the letter i\'m thinking of: \n')
    com_lett(my_letter)
    print(show_update())

if __name__ == "__main__": 
    main()
    # Falta hacer que el cambio lo haga sobre las lineas de arriba y despues meter todo en un while loop y
    # hacer que no muestre el la palabra none. 