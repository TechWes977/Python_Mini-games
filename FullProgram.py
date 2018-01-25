#
#
#
#
#
#
#
#
#
#
#
################################################################################
##########BELOW ARE ALL OF THE NEEDED IMPORTS AND VARIABLE DECLARATOINS:########
################################################################################
import random
score = 0

################################################################################
########################BELOW ARE ALL OF THE FUNCTIONS##########################
################################################################################
def main_menu(userName,score,title):
    """ To Bring the User to the Main Menu, Where they can then go to
        subsequent places. """
    while True:
        print("_______________________________________________________________")
        print("{:^82s}".format(title))
        print()
        print("Hello, {}! Your score is: {}".format(userName,score))
        print()
        print("1) Guess the Number")
        print("2) Rock, Paper, Scissors")
        print("3) Zombie Survival")
        print("4) Submit Score")
        print("5) Switch Player")
        print("6) Help")
        try:
            mainMenu_choice = str(input(">>"))

            if mainMenu_choice == "1":
                guess_the_number(userName,score,"Guess the Number")
            elif mainMenu_choice == "2":
                rock_paper_scissors(userName,score,"Rock, Paper, Scissors")
            elif mainMenu_choice == "3":
                zombie_survival(userName,score,"Zombie Survival")
            elif mainMenu_choice == "4":
                #print("This will submit user's score to highscore file")
                print("score: {}".format(score))
            elif mainMenu_choice == "5":
                break
            elif mainMenu_choice == "6":
                help_menu(userName,score,"Help Menu")
            else:
                print("Invalid Choice. Try Again.")
            print("----------------------------------------------------")

        except ValueError:
            print("Value Error")
        except NameError:
            print("Name Error")
        except TypeError:
            print("Type Error")        
################################################################################
def rock_paper_scissors(userName,score,title):
    """ Plays out 5 rounds of rock, paper, scissors, keeping score for each
        round, and then returns user to the main menu w/ an updated score. """
    print("_______________________________________________________________")
    print("{:^82s}".format(title))
    optionsList = [("Rock","rock","1",1),("Paper","paper","2",2),("Scissors","scissors","3",3),("Quit","quit","4",4,"Quit to main menu","quit to main menu","Quit to Main Menu")]
    counter = 0
    while counter <= 5:
        print("Choose one:")
        print()
        print("1)Rock")
        print("2)Paper")
        print("3)Scissors")
        print("4)Quit to Main Menu")
        choice = str(input(">>"))
        print("------------------------")
        if choice in optionsList[0]:
            print("You chose Rock")
            choice = optionsList[0]

        elif choice in optionsList[1]:
            print("You chose Paper")
            choice = optionsList[1]

        elif choice in optionsList[2]:
            print("You chose Scissors")
            choice = optionsList[2]

        elif choice in optionsList[3]:
            print("Returning to Main Menu...")
            break

        else:
            print("invalid choice")
            continue
        
        AIchoice = random.choice(optionsList[0:3])
        if AIchoice == optionsList[0]:
            print("Computer chose Rock")
        elif AIchoice == optionsList[1]:
            print("Computer chose Paper")
        elif AIchoice == optionsList[2]:
            print("Computer chose Scissors")

        if ((choice == optionsList[0]) and (AIchoice == optionsList[0])):
            print("You Tied")
        elif ((choice == optionsList[0]) and (AIchoice == optionsList[1])):
            print("You Lost.")
            score -= 1
        elif ((choice == optionsList[0]) and (AIchoice == optionsList[2])):
            print("You Win!")
            score += 2
            
        elif ((choice == optionsList[1]) and (AIchoice == optionsList[0])):
            print("You Win!")
            score += 2
        elif ((choice == optionsList[1]) and (AIchoice == optionsList[1])):
            print("You Tied")
        elif ((choice == optionsList[1]) and (AIchoice == optionsList[2])):
            print("You Lost.")
            score -= 1
            
        elif ((choice == optionsList[2]) and (AIchoice == optionsList[0])):
            print("You Lost.")
            score -= 1
        elif ((choice == optionsList[2]) and (AIchoice == optionsList[1])):
            print("You Win!")
            score +=1
        elif ((choice == optionsList[2]) and (AIchoice == optionsList[2])):
            print("You Tied")

        else:
            print("outcome not determined- Try Again.")
            continue
        counter += 1
        print("------------------------")
    print("------------------------")
    print("Your score is now: {}".format(score))
    input("(Press Enter to Continue)")
    return main_menu(userName,score,"Main Menu")
################################################################################
def guess_the_number(userName,score,title):
    print("{:^82s}".format(title))
    answer = ((random.random() * 100) + 1)
    try:
        guess = input("input an integer between 1-100: ")
        counter = 0
        answer = int(answer)
        guess = int(guess)
        while 0 < guess < 101:
            if guess > answer:
                print("Too high! Try guessing a little lower...")
                print(" ")
                counter += 1
            elif guess < answer:
                print("Too low... try guessing a little higher!")
                print(" ")
                counter += 1
            else:
                print("Nice! You got it!")
                print(" ")
                counter += 1
                score += 10
                print('It took you',counter, 'times to guess correctly')
                if counter <= 1:
                    print("Are you psychic?! You got it right on your first try!")
                    score += 5
                elif 1 < counter <= 6:
                    print("Not too bad!")
                    score += 3
                elif 6 < counter <= 9:
                    print("Your guessing skills are about average")
                    score += 2
                elif 9 < counter <= 12:
                    print("You're not a very good guesser tbh...")
                    score += 1
                else:
                    print("yeah, don't quit your day job buddy")
                    score -= 3
                break
            guess = int(input("Enter a new number between 1-100: "))
        print()
        print("Your score is now: {}".format(score))
        input("Press Enter to return to the Main Menu")
        main_menu(userName,score,"Main Menu")
    except TypeError:
        print("Type Error")
    except NameError:
        print("Name Error")
    except ValueError:
        print("Value Error")
################################################################################
def help_menu(userName,score,title):
    while True:
        print("_______________________________________________________________")
        print("{:^82s}".format(title))
        print("Choose one: ")
        print()
        print("1) Guess the Number ")
        print("2) Rock Paper Scissors")
        print("3) Errors")
        print("4) Score/Switching Users")
        print("5) Back to Main Menu")
        try:
            helpMenu_choice = str(input(">>"))
            if helpMenu_choice == "1":
                print("-------------------------------------------------------")
                print("In this game, a random number will be generated between 0 and 100.")
                print("The user will continue to try and guess the number.")
                print("After each incorrect guess, the user will be told to guess higher or lower.")
                print("When the user does guess the correct number, and will be told how many tries it took.")
                print("The fewer guesses it took, the more points the user will have added to his/her score.")
                print("-------------------------------------------------------")
                input("(Press Enter to continue)")
                continue

            elif helpMenu_choice == "2":
                print("-------------------------------------------------------")
                print("This is text-based version of the popular game 'Rock,Paper,Scissors'")
                print("The user will have turns to play against a computer opponent.")
                print("The user will be shown what he/she chose, as well as what the computer picked.")
                print("The user will be given 2 points for a win, no points for a tie, and will lose 1 point for a loss.")
                print("After the 5 turns are up, the user will be returned to the main menu.")
                print("-------------------------------------------------------")
                input("(Press Enter to continue)")
                continue

            elif helpMenu_choice == "3":
                print("-------------------------------------------------------")
                print("Using exception handling, most errors have been taken into account.")
                print("However, if an error were to occur, it is most likely due to user input.")
                print("Make sure to only input what the program is asking for.")
                print("-------------------------------------------------------")
                input("(Press Enter to continue)")
                continue

            elif helpMenu_choice == "4":
                print("-------------------------------------------------------")
                print("Score is tracked globally. If the user were to change users, the score is reset to 0")
                print("At any time, the user can submit his/her score to the 'highscores' file from the main menu.")
                print("This will reset his/her score to 0, but will include his/her name and score in the highschores file.")
                print("Note: as of now, if you try and switch users while you have score, switching once will just reset your score,")
                print("and if you try to switch when you have 0 score, then it will allow you to enter a new user's name.")
                print("-------------------------------------------------------")
                input("(Press Enter to continue)")
                continue

            elif helpMenu_choice == "5":
                main_menu(userName,score,"Main Menu")
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
################################################################################
def zombie_survival(userName,score,title):
    print("{:^82s}".format(title))
    ##begin phase 1
    inp1 = input("You wake up in a hospial bed; the  power is out and there seems to be nobody around. \nMake a choice: a)Get up and explore\
    \n               b)Call a friend \n               c)Go back to sleep\n") #spacing for a nice layout
    #if for choice 1
    if inp1 == "a":
        #begin phase 2
        inp2 = input("You get out of bed and stretch. You feel exhausted. There is nobody in the room and the place seems way to quiet.\n\
        a)Make your way outside\n    b)Scream for help\n")
        #if for choice 2
        if inp2 == "a":
            inp3 = input ("You finally make it through the abandoned hostpital and get to the open air. There is not a single person in sight.\
     It's like everything and everyone just vanished.\n    a)Go to police station\n    b)Go home\n")
            #if for choice 3
            if inp3 == "a":
                print("You finally arrive at the police station. Slowly walking up to the door, you hear noises inside.\
     The door is chained. When you're almost there the door creaks open. A man emerges and ushers you inside. He explains that\
      they are the only remaing civilians alive in the city. You join them; eager to begin a new life.\n")
                #end of 1st sequence
                wait = input("Press any key to continue...\n")
                print("CONGRATULATIONS! You have survived!")
                score += 1
                input("(Press Enter to continue)")
                main_menu(userName,score,"Main Menu")
            if inp3 == "b":
                inp4 = input("When you make it to your house, you find two zombies in your front yard.\n a)Take your chances and try to run past\n\
     b)Try to find help at the police station\n")
                #if for choice 4
                if inp4 == "a":
                    print("As you are running for the door, your untied shoelace trips you and you fall. The zombies come running\
    and are on top of you before you can even stand.")
                    #end of 2nd sequence
                    wait = input("Press any key to continue...\n")
                    print("Sorry, you did not survive...")
                    input("(Press Enter to continue)")
                    main_menu(userName,score,"Main Menu")
                if inp4 == "b":
                    print("You finally arrive at the police station. Slowly walking up to the door, you hear noises inside.\
     The door is chained. When you're almost there the door creaks open. A man emerges and ushers you inside. He explains that\
      they are the only remaing civilians alive in the city. You join them; eager to begin a new life.\n")
                    #end of 3rd sequence
                    wait = input("Press any key to continue...\n")
                    print("CONGRATULATIONS! You have survived!")
                    score += 1
                    input("(Press Enter to continue)")
                    main_menu(userName,score,"Main Menu")
        #other if for choice 2
        if inp2 == "b":
            print('You scream out of desperation that someone will find you. All of a sudden you hear loud banging in the room next to you.\
    Three zombies come sprinting around the corner and you are trapped with no way to escape.\n')
            #end of 4th sequence
            wait = input("Press any key to continue...\n")
            print("Sorry, you did not survive...")
            input("(Press Enter to continue)")
            main_menu(userName,score,"Main Menu")
    #if for choice 1
    if inp1 == "b":
        inp2 = input("You call a friend to find out what's going on. Your friend is bunkered down and safe in his house.\
    He says he will explain everything when yall are together.\na)Try to get to the house\nb)Ask your friend to come get you\n")
        #if for choice 2
        if inp2 == "a":
            print("On the way to the friends house a large group of zombies begin to run toward you and chase you. Right as you get to\
    your friend's block, you trip and fall while looking backwards. The zombie hoard overwhelms you.")
            #end of 5th sequence
            wait = input("Press any key to continue...")
            print("Sorry, you did not survive...")
            input("(Press Enter to continue)")
            main_menu(userName,score,"Main Menu")
        #if for choice 2
        if inp2 == "b":
            print("You wait for your friend to arrive. Whenever your friend gets there, he runs toward you and begins to \
    lightly shake you,yelling wake up. You wake up in your bed. It's time for school!")
            #end of 6th sequence
            wait = input("Press any key to continue...\n")
            print("CONGRATULATIONS! You completed the game.")
            score += 1
            input("(Press Enter to continue)")
            main_menu(userName,score,"Main Menu")
    #if for choice 1
    if inp1 == "c":
        print("You decide to go back to sleep. You wake up in your room, facing your alarm clock. 7:45am. Time to \
    get ready for school!")
        #end of 7th sequence
        wait = input("Press and key to continue...\n")
        print("CONGRATULATIONS! You completed the game.")
        score += 1
        input("(Press Enter to continue)")
        main_menu(userName,score,"Main Menu")




































################################################################################
########################BELOW IS THE INITIAL PROGRAM:###########################
################################################################################
while True:
    try:
        userName = str(input("Enter your name: "))
        print()
        main_menu(userName,score,"Main Menu")
        
    except ValueError:
        print("Value Error")
        continue
    except NameError:
        print("Name Error")
        continue
    except TypeError:
        print("Type Error")   
        
