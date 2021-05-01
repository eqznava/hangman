import random

def read():
    words = []
    with open('./archivos/data.txt', 'r', encoding = 'utf-8' ) as file:
        for line in file:
            words.append(line)
        random_word = random.choice(words)
        return random_word

#Convert to comprehension function
def random_words_to_list(random_word):
    word_to_list = list(random_word)
    word_to_list.pop()
    return word_to_list


def compare(word_to_list, my_list_word):
    if word_to_list == my_list_word:
        print('\nYou did, !!! wow your a genius !!!')
    else:
        print('Sorry your wrong bad luck')


def run():
    w = random_words_to_list(read())
    print(w)
    my_word = input('Intenta adivinar la palabra que estoy pensando:\n')
    my_list_word = list(my_word)
    compare(w, my_list_word)
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