import random
score = 0
################################################################################
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
    print("Your score is now: {}".format(score))
    input("Press Enter to return to the Main Menu")
    #Enter the main_menu Function here
except TypeError:
    print("Type Error")
except NameError:
    print("Name Error")
except ValueError:
    print("Value Error")

