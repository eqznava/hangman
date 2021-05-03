import random

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
    for i in range(len(lts)):
        all_index.append('_')
    for i in all_index:
        print(i, end = ' ')
    

def com_lett(my_letter):
    word_to_list = []
    with open('C:/Users/natif/Escritorio/papa/Python/python_intermedio/proyecto_final/archivos/random_word.txt','r', encoding='utf-8') as file:
        for line in file:
            word_to_list = line
            wtl = list(word_to_list)
            wtl.pop()
    for  lett in word_to_list:
        if lett == my_letter:
            print('La encontre !!!')
        else:
            print('No hay ninguna coinsidencia.')


def run():
    # w = random_words_to_list(read())
    print(read())
    print('\n')
    transform_characters(transform_to_list())
    print('\n')
    my_letter = input('Try to guess the letter i\'m thinking of:\n')
    com_lett(my_letter)


if __name__ == '__main__':
    run()