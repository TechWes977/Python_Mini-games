title = "Help Menu"
################################################################################
while True:
    print("{:^82s}".format(title))
    print("Choose one: ")
    print()
    print("1) Guess the Number ")
    print("2) Rock Paper Scissors")
    print("3) Game 3")
    print("4) Game 4")
    print("5) Game 5")
    print("6) Game 6")
    print("7) Errors")
    print("8) Score/Switching Users")
    print("9) Back to Main Menu")
    try:
        helpMenu_choice = str(input(">>"))
        if helpMenu_choice == "1":
            print("In this game, a random number will be generated between 0 and 100.")
            print("The user will continue to try and guess the number.")
            print("After each incorrect guess, the user will be told to guess higher or lower.")
            print("When the user does guess the correct number, and will be told how many tries it took.")
            print("The fewer guesses it took, the more points the user will have added to his/her score.")
            print()
            input("(Press Enter to continue)")
            continue

        elif helpMenu_choice == "2":
            print("This is text-based version of the popular game 'Rock,Paper,Scissors'")
            print("The user will have turns to play against a computer opponent.")
            print("The user will be shown what he/she chose, as well as what the computer picked.")
            print("The user will be given 2 points for a win, no points for a tie, and will lose 1 point for a loss.")
            print("After the 5 turns are up, the user will be returned to the main menu.")
            input("(Press Enter to continue)")
            continue

        elif helpMenu_choice == "3":
            print("write description of Game 3 here")
            input("(Press Enter to continue)")
            continue

        elif helpMenu_choice == "4":
            print("Game 4 description here")
            input("(Press Enter to continue)")
            continue

        elif helpMenu_choice == "5":
            print("game 5 descrip. here.")
            input("(Press Enter to continue)")
            continue

        elif helpMenu_choice == "6":
            print("game 6 descrip here.")
            input("(Press Enter to continue)")
            continue

        elif helpMenu_choice == "7":
            print("Using exception handling, most errors have been taken into account.")
            print("However, if an error were to occur, it is most likely due to user input.")
            print("Make sure to only input what the program is asking for.")
            print()
            input("(Press Enter to continue)")
            continue

        elif helpMenu_choice == "8":
            print("Score is tracked globally. If the user were to change users, the score is reset to 0")
            print("At any time, the user can submit his/her score to the 'highscores' file from the main menu.")
            print("This will reset his/her score to 0, but will include his/her name and score in the highschores file.")
            print("Note: as of now, if you try and switch users while you have score, switching once will just reset your score,")
            print("and if you try to switch when you have 0 score, then it will allow you to enter a new user's name.")
            input("(Press Enter to continue)")
            continue

        elif helpMenu_choice == "9":
            #Call main_menu(userName,score,"Main Menu")
            break
            

        else:
            print("Invalid Input: Try Again.")
            continue

    except NameError:
        print("Name Error")
    except TypeError:
        print("Type Error")
    except ValueError:
        print("Value Error")
        
        

