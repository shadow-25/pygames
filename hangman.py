import random
def list_to_word(list):
    new_word=' '.join(map(str,list))
    print(new_word)
def word_1(word):

    word=random.choice(word)
    return word

def game():
    # intro
    print("Welcome to the game")
    print("You Get Only 5 guesses")


    # word list
    word_list=['hacker','game','anime','mobile','cricket','apple', 'banana','cherry','date','grape','kiwi','lemon','mango','orange','papaya','raspberry','strawberry','random','cpu','gpu','moniter','keybord']
    word_list= [word.upper() for word in word_list]


    score=0
    guess=5
    # choosing random word from list
    word=word_1(word_list)
    # for user to guess word
    user_word=[]
    for i in word:
        user_word.append('_')
    list_to_word(user_word)

    # user input 
    while '_'  in user_word:
        if guess==0:
            print("Game Over")
            print(f"You score {score}")
            break
        
        W=input("Enter the letter ").capitalize()
        for i,letter in enumerate(word):
            if letter==W:
                user_word.pop(i)
                user_word.insert(i,W)
                score+=1
        if W not in word:
            guess-=1
        if "".join(map(str,user_word)) == word:
            print("*****Congrats You Got The Word Right*****")
            print("You Get 5 Extra Points ")
            score+=5
            word=word_1(word_list)
            user_word=[]
            for i in word:
                user_word.append('_')
        list_to_word(user_word)
        print(f"Your current score is {score}")
        print(f"Number of guesses left is {guess}")
    with open(r"E:\codes\Python\py game\hm_highscore.txt","r") as f:
        highscore=int(f.read())
    if (score>highscore):
        print("You have just broke the highscore!")
        with open(r"E:\codes\Python\py game\hm_highscore.txt","w") as f:
            f.write(str(score))




game()