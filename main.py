import string
import random
import discord
from discord.ext import commands
from discord import Interaction

#  *** Encoding a message ***
def encoding(str=''):
    encoded_str = ''
    word_lst = str.split()

    for word in word_lst:
        first_char = word[0]

        #  Putting first character to last
        if len(word) >= 3:
            word = word[1:] + first_char
        else:
            word = word[::-1]

        #  Adding random char at start and end
        first_rndm = [random.choice(string.ascii_lowercase) for _ in range(3)]
        last_rndm = [random.choice(string.ascii_lowercase) for _ in range(3)]

        for i in range(3):
            word = first_rndm[i] + word + last_rndm[i]

        # Joining each word in sentence
        encoded_str += word + ' '

    return encoded_str

#  *** Encoding a message ***
def decoding(str=''):
    decoded_str = ''
    word_lst = str.split()

    for word in word_lst:

        #  Removing random char at start and end
        word = word[3:-3]

        #  Putting last character to start
        last_char = word[-1]

        if len(word) >= 3:
            word = last_char + word[:-1]
        else:
            word = word[::-1]

        # Joining each word in sentence
        decoded_str += word + ' '

    return decoded_str

def user_input():
    print('\n---------Encoder and Decoder---------')

    try:
        opt = int(input('Enter 1 for encode 2 for decode or 0 for exist: '))
    except ValueError:
        print(f'{ValueError}: Type integer only\n')
        user_input()
        return

    match opt:
        case 1:
            message = input('Enter message: ')
            encoding(message)
            user_input()
        case 2:
            message = input('Enter message: ')
            decoding(message)
            user_input()
        case 0:
            print("Thanks for using me ^^\n")
            return
        case _:
            print('Try to choose above mentioned option\n')
            user_input()


if __name__ == '__main__':
    user_input()

