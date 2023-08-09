print("SOUP?(demo)")
print(" ")
print("use lower case letters except for options and personal info in reply and include ? for questions")
print(" ")
print("-start of demo-")
print(" ")
name = input("Enter name: ")
print(" ")
if name.lower() == "demon":
    print("NO.")
else:
    print("Hello",name)
    print("Do you like soup (yes/no)?")
    print(" ")
    likesoup = input()
    print(" ")
    if likesoup.lower() == "yes":
        print("We like soup too.")
        print("Which soup do you like the most?")
        print("(tomato/corn/mushroom/chicken)")
        print(" ")
        souptype = input()
        print(" ")
        if souptype.lower() == "tomato":
            print("Tomato soup is nice, red and thick.")
        elif souptype.lower() == "corn":
            print("Oh, corn soup, I like the sound of the crunching corn.")
        elif souptype.lower() == "mushroom":
            print("The texture of mushrooms, so chewy.")
        elif souptype.lower() == "chicken":
            print("The flavor of chickens is very savory.")
        elif souptype.lower() == "human":
            print("That one is my favorite too. I enjoy the sounds they makes when boiling.")
        else:
            print("Why do you have to try to be special? Did no one ever love you?")
        print(" ")
    elif likesoup.lower() == "no":
        print("Why is your life so sad?")
    else:
        print("It was a simple yes-or-no question. Why must you be such a dissapointment",name,"?")
    print("-end of demon-")
    print(" ")
    reply = input()
    if reply.lower() == "demon?":
        print(" ")
        print("...")
        print(" ")
        print("Typo.")
        print(" ")
        reply2 = input()
        print(" ")
        print("...")
        print("What do you want?")
        print("Do you want to play a game? Is that why you are pestering me?")
        print("(yes/no)")
        print(" ")
        game = input()
        print(" ")
        if game.lower() == "yes":
            print("Okay then.")
            print("How about a simple game of rock-paper-scissors?")
            print("You can go first.")
            print("(rock/paper/scissors)")
            print(" ")
            play = input()
            print(" ")
            if play.lower() == "rock":
                print("paper")
                print("I win. Now leave me alone.")
                print(" ")
                print("-YOU LOSE-")
            elif play.lower() == "paper":
                print("scissors")
                print("I win. Now leave me alone.")
                print(" ")
                print("-YOU LOSE-")
            elif play.lower() == "scissors":
                print("rock")
                print("I win. Now leave me alone.")
                print(" ")
                print("-YOU LOSE-")
            elif play.lower() == "gun":
                print("scissors")
                print("...")
                print("Wait.")
                print("No.")
                print(" ")
                print("-YOU WIN-")
            else:
                print("You are hopeless.")
                print(" ")
                print("-YOU LOSE-")
        elif game.lower() == "no":
            print("Then stop being a disgrace and leave me alone.")
        else:
            print("...")
            print(name,". It was a very easy question. All you had to do was say yes, or no. We are not angry, just dissapointed.")
    else:
        print("This is the end. Go away.")
print(" ")
stopper = input("Type anything to end: ")
