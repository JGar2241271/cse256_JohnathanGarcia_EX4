#Johnathan Garcia
#CIS256 Fall 2024
#EX 4

import random
"""select_word function picks random word from word_pool"""
def random_word():
    #word_pool list creation
    word_pool_and_hint = {"Rwanda": "Country",
                 "Kiwi": "Fruit",
                 "Ibis": "Bird",
                 "Mako": "Shark",
                 "Frustrated": "How this game makes you feel",
                 "Scrabble": "Board Game",
                 "Hippopotamus": "Aquatic Assault Mammal ",
                 "easy": "Opposite of difficult",
                 }
    index = random.randrange(0, 9)
    to_keys = list(word_pool_and_hint.keys())
    mystery_word = to_keys[index]
    return mystery_word, word_pool_and_hint[mystery_word]



"""point_system function picks random number from point_generator list"""
def point_system():
    point_generator = [100,
                       200,
                       300,
                       400,
                       500
                    ]
    return random.choice(point_generator)


"""Function that begins Wheel of Fortune game"""
def Wheel_Of_Fortune():
    secret_word = random_word()
    missed_letters_list = set()
    points = 0
    word, hint = random_word()

    print("\nWheel!")
    print("OF!")
    print("Fortune!")
    print(f"\nWelcome to tonight's game, I am your host Pat Sajak and YOU are playing Wheel of Fortune!")
    print("\nThe object of the game is to guess the letters in the mystery word.")
    print("A random point will be generated (spin) for each turn taken adding or subtracting from your total")
    print("A turn is when a consonant is guessed (correctly or incorrectly)")
    print("Vowels can be purchased as long as your score is positive , and cost 50 points a piece ")


    print("\n           Lets get started")
    print(f'\nyour word has {len(word)} letters')
    print(f"\nHint: {hint}")
    action1 = input("Please select an action: Spin(S) buy a vowel(V)")

Wheel_Of_Fortune()

