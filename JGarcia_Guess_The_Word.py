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
print(random_word()) # check function to see random.choice from word_pool - Delete later
def point_system():
    point_generator = [100,
                       200,
                       300,
                       400,
                       500
    ]
    return random.choice(point_generator)
print(point_system())



