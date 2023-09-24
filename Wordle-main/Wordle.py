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

user_stats = {
    '5 guesses': 0,
    '4 guesses': 0,
    "3 guesses": 0,
    "2 guesses": 0,
    "1 guess": 0
    }

color_choice = simpledialog.askstring("Color Scheme", "Choose color scheme (1 for Normal, 2 for Fancy): ")
    # Check the user's choice and set colors accordingly
if color_choice == "1": 
    CORRECT = CORRECT_COLOR
    PRESENT = PRESENT_COLOR
    MISSING = MISSING_COLOR
else:
    CORRECT = CORRECT_COLOR2
    PRESENT = PRESENT_COLOR2
    MISSING = MISSING_COLOR2

def Wordle():
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
                        #changing the color if the letter is guessed correctly
                        wordActual_list[i] = gw.set_square_color(rowCurrent, i, CORRECT)

                    elif guess_the_letter in wordActual and guess_the_letter != wordActual[i]:
                        wordActual_list[i] = gw.set_square_color(rowCurrent, i, PRESENT)

                    else:
                        wordActual_list[i] = gw.set_square_color(rowCurrent, i, MISSING)
                    

                if wordCurrent == wordActual:
                    gw.show_message("Congratulations! It took you " + str(rowCurrent + 1) + " guess(es)!")
                    #gw.add_enter_listener(enter_action)
                    #gw.window.set_key_enabled(False)
                    
                    #loading up the user_stats dictionary with game results
                    if (rowCurrent + 1) == 1:
                        user_stats["1 guess"] += 1
                    elif (rowCurrent + 1) == 2:
                        user_stats["2 guesses"] += 1
                    elif (rowCurrent + 1) == 3:
                        user_stats["3 guesses"] += 1
                    elif (rowCurrent + 1) == 4:
                        user_stats["4 guesses"] += 1
                    else:
                        user_stats["5 guesses"] += 1

                    #display the results when the player wins
                    stats_message = ("Player 1's Statistics: " + "\n" + 
                        "5 guesses: " + str(user_stats['5 guesses']) + "\n" +
                        "4 guesses: " + str(user_stats["4 guesses"]) + "\n" +
                        "3 guesses: " + str(user_stats["3 guesses"]) + "\n" +
                        "2 guesses: " + str(user_stats["2 guesses"]) + "\n" +
                        "1 guess: " + str(user_stats["1 guess"])
                        )
                    messagebox.showinfo("Player Statistics: ", stats_message)


                else:

                    if rowCurrent == N_ROWS - 1:
                        gw.show_message('Sorry, you lost! The word was "' + wordActual.upper() + '".')
                        #gw.add_enter_listener(enter_action)
                        #gw.window.set_key_enabled(False)
                        

                    else:
                        gw.set_current_row(rowCurrent + 1)

            #If the typed word is not legitimate, display "Not in word list" using the show_message method
            else:
                gw.show_message("Not in wordlist")
                
        gw.show_message("Guess the word to win!")  
        #gw.show_message("The correct word is " + wordActual.upper())
        #Use the add_enter_listener method to respond to the ENTER key press event
        #Call gw.add_enter_listener(enter_action) to set up a function (enter_action) to be called when ENTER is pressed
        gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    Wordle()
