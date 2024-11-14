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
    used_letters_list = set()
    points = 0
    word, hint = random_word()

    print("\nWheel!")
    print("OF!")
    print("Fortune!")
    print(f"\nWelcome to tonight's game, I am your host Pat Sajak and YOU are playing Wheel of Fortune!")
    print("\nThe object of the game is to guess the letters in the mystery word.")
    print("A random point will be generated for each guess taken adding or subtracting from your total")
    print("A turn is when a consonant is guessed (correctly or incorrectly)")
    print("Vowels can be purchased as long as your score is positive , and cost 50 points a piece ")
    print("Solving the puzzle correctly will end the game, Solving incorrectly will lose points")


    print("\n           Lets get started")
    print(f'\nyour word has {len(word)} letters')
    print(f"Word: {display_word(word.lower(), used_letters_list)}") #displays mystery word progress
    print(f"\nHint: {hint}")
    action1 = input("\nPlease select an action: Guess(G), buy a vowel(V), Solve(S)").lower()

    #While loop, core game function
    while True:
        print(f"\nCurrent word: {display_word(word.lower(), used_letters_list)}")
        print(f"Current points: {points}")

        #If loop for guessing words
        if action1 == "g":
            point = point_system()
            print(f"\nfor {point} points")
            Consonant = input("\nplease select a consonant").lower()

            #error catcher if user does not enter anything
            if len(Consonant) != 1:
                print("\nPlease select a single consonant")
                continue
            #error catcher if user does not enter a letter
            if not Consonant.isalpha():
                print("\nPlease select a letter")
                continue

            #error catcher to see if letter has been used
            elif Consonant in used_letters_list:
                points = points - point
                print("\nLetter has already been guessed")
                print(f"Current word: {display_word(word.lower(), used_letters_list)}")
                print(f"Hint: {hint}")
                print(f"Current points: {points}")
                action1 = input("\nPlease select an action: Guess(G), buy a vowel(V), Solve(S)").lower()
            #checking if letter in mystery word
            elif Consonant in word.lower():
                used_letters_list.add(Consonant)
                points = points + point
                print(f"\nCorrect! The letter {Consonant.upper()} is in mystery word. plus {point} points")
                print(f"Current word: {display_word(word.lower(), used_letters_list)}")
                print(f"Hint: {hint}")
                print(f"Current points: {points}")
                action1 = input("\nPlease select an action: Guess(G), buy a vowel(V), Solve(S)").lower()
            #catch for letters not in mystery word
            else:
                used_letters_list.add(Consonant)
                points = points - point
                print(f"\nOops, The letter {Consonant.upper()} is NOT in mystery word. Minus {point} points")
                print(f"Current word: {display_word(word.lower(), used_letters_list)}")
                print(f"Hint: {hint}")
                print(f"Current points: {points}")
                action1 = input("\nPlease select an action: Guess(G), buy a vowel(V), Solve(S)").lower()
        #if loop for vowels if v selected in action1
        elif action1 == "v" and points >= 50:
            vowel = input("\nPlease select a vowel").lower()
            if len(vowel) != 1:
                print("\nPlease select a single vowel")
                continue
            if not vowel.isalpha():
                print("\nPlease select a letter")
                continue
            elif vowel in used_letters_list:
                points = points - point
                print("\nLetter has already been guessed")
                print(f"Current word: {display_word(word.lower(), used_letters_list)}")
                print(f"Hint: {hint}")
                print(f"Current points: {points}")
                action1 = input("\nPlease select an action: Guess(G), buy a vowel(V), Solve(S)").lower()
            elif vowel in word.lower():
                used_letters_list.add(vowel)
                points = points - 50
                print(f"\nCorrect! The letter {vowel.upper()} is in mystery word.")
                print(f"Current word: {display_word(word.lower(), used_letters_list)}")
                print(f"Hint: {hint}")
                print(f"Current points: {points}")
                action1 = input("\nPlease select an action: Guess(G), buy a vowel(V), Solve(S)").lower()
            else:
                used_letters_list.add(vowel)
                points = points - 50
                print(f"\nOops, The letter {vowel.upper()} is NOT in mystery word.")
                action1 = input("\nPlease select an action: Guess(G), buy a vowel(V), Solve(S)").lower()
        elif action1 == "v" and points <= 50:
            print("\nYou do not have enough points to buy a vowel")
            action1 = input("\nPlease select an action: Guess(G), buy a vowel(V), Solve(S)").lower()
        elif action1 == "s":
            point = point_system()
            print(f"\nfor {point} points")
            solve = input("\nwhat is the mystery word?").lower()
            if solve != word.lower():
                points = points - point
                print(f"\nOops,  {solve.upper()} is NOT in mystery word.")
                print(f"Current word: {display_word(word.lower(), used_letters_list)}")
                print(f"Hint: {hint}")
                print(f"Current points: {points}")
                action1 = input("\nPlease select an action: Guess(G), buy a vowel(V), Solve(S)").lower()
            elif solve == word.lower():
                points = points + point
                print(f"\nWinner, Winner, Chicken Dinner!.")
                print(f"Points total: {points}")
                print("Thank you for playing!")
                break
        else:
            print("\ninvalid entry")
            action1 = input("\nPlease select an action: Guess(G), buy a vowel(V), Solve(S)").lower()

Wheel_Of_Fortune()

