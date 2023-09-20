# File: Wordle.py

"""
Wordle Game. 9/13/23 Team 4
"""
#Milestone 1 & 2 Finished -->

import random
from tkinter import simpledialog, messagebox
from WordleGraphics import CORRECT_COLOR, CORRECT_COLOR2, PRESENT_COLOR, PRESENT_COLOR2, MISSING_COLOR, MISSING_COLOR2
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

total_guesses = 0

color_choice = simpledialog.askstring("Color Scheme", "Choose color scheme (1 for Normal, 2 for Fancy): ")
    # Check the user's choice and set colors accordingly
if color_choice == "1": 
    CORRECT = CORRECT_COLOR
    PRESENT = PRESENT_COLOR
    MISSING = MISSING_COLOR
else:
    CORRECT = CORRECT_COLOR2
    PRESENT = PRESENT_COLOR2
    MISSING = MISSING_COLOR

def Wordle():

    # color_choice = messagebox.askstring("Color Scheme", "Choose color scheme (1 for Normal, 2 for Fancy): ")
    # # Check the user's choice and set colors accordingly
    # if color_choice == "1": 
    #     CORRECT = CORRECT_COLOR
    #     PRESENT = PRESENT_COLOR
    #     MISSING = MISSING_COLOR
    # else:
    #     CORRECT = CORRECT_COLOR2
    #     PRESENT = PRESENT_COLOR2
    #     MISSING = MISSING_COLOR
        


        # Startup code
        gw = WordleGWindow()
        wordActual = random.choice(FIVE_LETTER_WORDS)

        #Write the enter_action function. This function will be called when the user presses ENTER
        def enter_action(s):
            rowCurrent = gw.get_current_row()
            wordCurrent = ""

            #Use a loop that runs from column 0 to N_COLS (which is 5) to fill each box with a letter from the selected word
            for letter in range(0, N_COLS):
                letterCurrent = gw.get_square_letter(rowCurrent, letter)
                wordCurrent += letterCurrent
            wordCurrent = wordCurrent.lower()

            #Inside enter_action, check if the typed word is a legitimate English word
            #need a way to validate words against a list of legitimate English words 
            if wordCurrent in FIVE_LETTER_WORDS:
                wordActual_list = list(wordActual)

                for i in range(N_COLS):
                    guess_the_letter = wordCurrent[i]

                    if guess_the_letter == wordActual[i]:
                        #wordActual_list[i] = None
                        #changing the color if the letter is guessed correctly
                        wordActual_list[i] = gw.set_square_color(rowCurrent, i, CORRECT)

                    elif guess_the_letter in wordActual_list:
                        wordActual_list[i] = gw.set_square_color(rowCurrent, i, PRESENT)

                    else:
                        wordActual_list[i] = gw.set_square_color(rowCurrent, i, MISSING)
                    

                if wordCurrent == wordActual:
                    gw.show_message("Congratulations! It took you " + str(rowCurrent + 1) + " guess(es)!")
                    #statistics
                    total_guesses = rowCurrent + 1
                    gw.remove_enter_listener(enter_action)
                    gw.window.set_key_enabled(False)

                else:

                    if rowCurrent == N_ROWS - 1:
                        gw.show_message('Sorry, you lost! The word was "' + wordActual.upper() + '".')
                        gw.remove_enter_listener(enter_action)
                        gw.window.set_key_enabled(False)

                    else:
                        gw.set_current_row(rowCurrent + 1)

            #If the typed word is not legitimate, display "Not in word list" using the show_message method
            else:
                gw.show_message("Not in wordlist")
            
        gw.show_message("The correct word is " + wordActual.upper())
        #Use the add_enter_listener method to respond to the ENTER key press event
        #Call gw.add_enter_listener(enter_action) to set up a function (enter_action) to be called when ENTER is pressed
        gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    Wordle()

    