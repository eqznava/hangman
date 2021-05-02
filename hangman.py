import random
##Me mostraba un error por no encontrar el archivo data.txt, estaba haciendo la funcion transform
#comente la funcion transform pero eso no era el problema.
# hay que descansar.
def read():
    words = []
    with open('./archivos/data.txt', 'r', encoding = 'utf-8' ) as file:
        for line in file:
            words.append(line)
        random_word = random.choice(words)
        return random_word


def random_words_to_list(random_word):
    word_to_list = list(random_word)
    word_to_list.pop()
    return word_to_list


# def transform(word_to_list):
#     #total_elements = len(word_to_list)
#     all_index = []
#     for i in range(len(word_to_list)):
#         all_index.append(i)
#     #print(all_index)
#     for i in all_index:
#         if i == i:
#             all_index[i] =='_'
#         print(all_index)

def compare(word_to_list, my_list_word):
    if word_to_list == my_list_word:
        print('\nYou did, !!! wow your a genius !!!')
    else:
        print('Sorry your wrong bad luck')


def run():
    w = random_words_to_list(read())
    print(w)
    print('\n')
    #transform(w)
    my_word = input('Try to guess the word i\'m thinking of:\n')
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