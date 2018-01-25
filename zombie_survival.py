#zombie survival text simulation for project
#Brandon Stehling
#def zombie_sim(userName,score,"ZOMBIE SURVIVAL"):
score = 0   #keeps a score for the game
print("ZOMBIE SURVIVAL SIMULATION\n")
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
            if inp4 == "b":
                print("You finally arrive at the police station. Slowly walking up to the door, you hear noises inside.\
 The door is chained. When you're almost there the door creaks open. A man emerges and ushers you inside. He explains that\
  they are the only remaing civilians alive in the city. You join them; eager to begin a new life.\n")
                #end of 3rd sequence
                wait = input("Press any key to continue...\n")
                print("CONGRATULATIONS! You have survived!")
                score += 1
    #other if for choice 2
    if inp2 == "b":
        print('You scream out of desperation that someone will find you. All of a sudden you hear loud banging in the room next to you.\
Three zombies come sprinting around the corner and you are trapped with no way to escape.\n')
        #end of 4th sequence
        wait = input("Press any key to continue...\n")
        print("Sorry, you did not survive...")
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
    #if for choice 2
    if inp2 == "b":
        print("You wait for your friend to arrive. Whenever your friend gets there, he runs toward you and begins to \
lightly shake you,yelling wake up. You wake up in your bed. It's time for school!")
        #end of 6th sequence
        wait = input("Press any key to continue...\n")
        print("CONGRATULATIONS! You completed the game.")
        score += 1
#if for choice 1
if inp1 == "c":
    print("You decide to go back to sleep. You wake up in your room, facing your alarm clock. 7:45am. Time to \
get ready for school!")
    #end of 7th sequence
    wait = input("Press and key to continue...\n")
    print("CONGRATULATIONS! You completed the game.")
    score += 1
    
