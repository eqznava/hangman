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


# Listo
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
    indices = []
    words = []
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/random_word.txt','r', encoding='utf-8') as file:
        for line in file:
            word_to_list = line
            wtl = list(word_to_list)
            wtl.pop()
    indices = [indice for indice, lett in enumerate(wtl) if lett == my_letter]
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/rw_transform.txt','r', encoding='utf-8') as file:
        for line in file:
            words = line
            w = list(words)
        #Me falta tomar los indices almacenados en indices y pedir que esos mismos indices los remplace 
        #por las letras que correspondan a dichos indices , para lo cual hay que hacer otro list comprehension 
        #para sacar las letras que corresponden a los indices y asi remplazarlos en el archivo rw_transform.
    print(w)

#Esta pendiente 
def run():    
    # my_list=[1,2,3]

    # while not my_list:
        print(read())
        print('\n')
        transform_characters(transform_to_list())
        print('\n')
        my_letter = input('Try to guess the letter i\'m thinking of:\n')
        com_lett(my_letter)


if __name__ == '__main__':
    run()