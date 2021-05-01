import random

def read():
    words = []
    with open('./archivos/data.txt', 'r', encoding = 'utf-8' ) as file:
        for line in file:
            words.append(line)
        random_word = random.choice(words)
    return random_word


def compare(random_word):
    word_to_list = list(random_word)
    print(word_to_list)


def run():
    print(read())
    compare(read())
    # print('---------------------------------------------------- H A N G M A N ----------------------------------------------------\n')
    # print('Hola (⌐■_■) tendras que adividar la palabra que estoy pensando ^_^ de lo contrario nuestro amigito morira ^_^\n')
    # print('\n')
    # print('_ _ _ _ _ _\n')
    # letter = (input('Ingresa una letra:\n'))
    # compare(word)
    # print('\n')
    # print('\n---------------------------------------------------------------------------------------------------------------------------')

if __name__ == '__main__':
    run()