#Johnathan Garcia
#CIS256 Fall 2024
#EX 4

import random
"""select_word function picks random word from word_pool"""
def random_word():
    #word_pool list creation
    word_pool = ["Rwanda",
                 "Kiwi",
                 "Ibis",
                 "Mako",
                 "Frustrated",
                 "Scrabble",
                 "Hippopotamus",
                 "easy",
    ]
    return random.choice(word_pool)

