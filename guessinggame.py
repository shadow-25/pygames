flag=True
while(flag):
    import random
    randNumber=random.randint(1,100)
    userguess=None
    guesses=0
    while(userguess!=randNumber):
        userguess=int(input("Enter your guess between (1,100): "))
        guesses+=1

        if(userguess==randNumber):
            print("You guessed right!")
        else:
            if (userguess>randNumber):
                print("You guessed it wrong! Enter a smaller number")
            else:
                print("You guessed it wrong! Enter a number larger")

    print(f"You guessed the number in {guesses} guesses")

    with open("E:\codes\Python\py game\highscore.txt","r") as f:
        highscore=int(f.read())

    if (guesses<highscore):
        print("You have just broke the highscore!")
        with open("E:\codes\Python\py game\highscore.txt","w") as f:
            f.write(str(guesses))
    wish=input("To Quit Enter q and to continue enter any other key : ")
    if(wish[0] == 'q'):
        flag=False
    else:
        flag=True

    
