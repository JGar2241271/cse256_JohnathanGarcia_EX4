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



"""point_system function picks random number from point_generator list"""
def point_system():
    point_generator = [100,
                       200,
                       300,
                       400,
                       500
                    ]
    return random.choice(point_generator)
print(point_system())

"""Function that begins Wheel of Fortune game"""
def Wheel_Of_Fortune():
    secret_word = random_word()
    missed_letters_list = set()
    points = 0

    print("Wheel!")
    print("of")
    print("Fortune!")
    print(f"\n Welcome to tonight's game, I am your host Pat Sajak and YOU are playing Wheel of Fortune!")
    print("\nThe object of the game is to guess the letters in the mystery word.")
    print("A random point will be generated (spin) for each turn taken adding or subtracting from your total")
    print("A turn is when a consonant is guessed (correctly or incorrectly)")
    print("Vowels can be purchased as long as your score is positive , and cost 50 points a piece ")


def Wheel_Of_Fortune():

    print("\n           Lets get started")
    action1 = input("Please select an action: Spin(S) buy a vowel(V)")