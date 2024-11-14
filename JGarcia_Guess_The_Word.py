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

"""function to display letters as they are used"""
def display_word(word, guessed_letters):
    display = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(display)

"""Function that begins Wheel of Fortune game"""
def Wheel_Of_Fortune():
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
    print(f"Word: {display_word(word.lower(), missed_letters_list)}")
    print(f"\nHint: {hint}")
    action1 = input("\nPlease select an action: Spin(S) buy a vowel(V)").lower()

    while True:
        print(f"\nCurrent word: {display_word(word.lower(), missed_letters_list)}")
        print(f"\nCurrent points: {points}")
        if action1 == "s":
            point = point_system()
            print(f"for {point} points")
            action2 = input("please select a consonant").lower()

            if len(action2) != 1:
                print("Please select a single consonant")
                continue
            elif not action2.isalpha():
                print("Please select a letter")
                continue
            elif action2 in missed_letters_list:
                print("\nLetter has already been guessed")
            elif action2 in word.lower():
                missed_letters_list.add(action2)
                points = points + point
                print(f"\nCorrect! The letter {action2.upper()} is in mystery word")
            else:
                missed_letters_list.add(action2)
                points = points - point
                print(f"\nOops, The letter {action2.upper()} is NOT in mystery word. Minus {point} points")
                break







Wheel_Of_Fortune()

