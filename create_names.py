'''Modulo para crear nombres al azar'''

import random

CONSONANTES = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q',
               'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z')

VOCALES = ('A', 'E', 'I', 'O', 'U')


def random_word(length):
    '''
    Function of return a random word
    parameters length:int Length of word
    return:str word
    '''
    word = ''
    con = length
    consonante_or_vocal = False  #False para Vocal. True para Consonante

    init_letter = random.randint(0, 1)
    if (init_letter == 1):
        #Letra inicial es vocal
        consonante_or_vocal = False
    else:
        #Letra inicial es consonante
        consonante_or_vocal = True

    while (con > 0):
        silaba_len = random.randint(1, 2)

        for i in range(1, silaba_len + 1):
            if (consonante_or_vocal):
                #Si la letra es Consonante
                if (silaba_len == 1):
                    break

                consonante_or_vocal = False
                word += asignar_consonante()

            else:
                #Si la letra es Vocal
                consonante_or_vocal = True
                word += asignar_vocal()

                if (silaba_len == 1):
                    con -= 1
                    break
            con -= 1
            if (con <= 0):
                break
    return word


def asignar_vocal():
    '''
    Funcion que devuelve una letra-vocal
    '''
    return VOCALES[random.randint(0, len(VOCALES) - 1)]


def asignar_consonante():
    '''
    Funcion que devuelve una letra-consonante
    '''
    return CONSONANTES[random.randint(0, len(CONSONANTES) - 1)]
