import random
score = 0
title = "Rock, Paper, Scissors"
##################################################################################################################################################################################
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
        print("Go to Main Menu")
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
################################################################################
#main_menu(userName,score,"Main Menu")
