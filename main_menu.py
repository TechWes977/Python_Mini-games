userName = "tester"
score = 0
title = "Main Menu"
################################################################################
while True:
    print("{:^82s}".format(title))
    print()
    print("Hello, {}! Your score is: {}".format(userName,score))
    print()
    print("1) Guess the Number")
    print("2) Rock, Paper, Scissors")
    print("3) Game 3")
    print("4) Game 4")
    print("5) Game 5")
    print("6) Game 6")
    print("7) Submit Score")
    print("8) Switch Player")
    print("9) Help")
    try:
        mainMenu_choice = str(input(">>"))

        if mainMenu_choice == "1":
            print("This will take the user to Guess the Number")
        elif mainMenu_choice == "2":
            print("This will take the user to Rock Paper Scissors")
        elif mainMenu_choice == "3":
            print("This will Take the User to Game 3")
        elif mainMenu_choice == "4":
            print("this will take the user to Game 4")
        elif mainMenu_choice == "5":
            print("this will take the user to Game 5")
        elif mainMenu_choice == "6":
            print("this will take the user to Game 6")
        elif mainMenu_choice == "7":
            print("This will submit user's score to highscore file")
        elif mainMenu_choice == "8":
            print("This will allow the user to be switched")
        elif mainMenu_choice == "9":
            print("This will display the help menu")
        else:
            print("Invalid Choice. Try Again.")
        print("----------------------------------------------------")


    except ValueError:
        print("Value Error")
    except NameError:
        print("Name Error")
    except TypeError:
        print("Type Error")        
