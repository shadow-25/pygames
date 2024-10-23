import random

def game(com,you):
    if com==you:
        return None
    #for rock
    elif com=="r":
        if you=="p":
            return True
        elif you=="s":
            return False
    #for paper
    elif com=="p":
        if you=="s":
            return True
        elif you=="r":
            return False
    #for scissor
    elif com=="s":
        if you=="r":
            return True
        elif you=="p":
            return False


print("Enter r for Rock, s for Scissor and p for Paper")
rounds=int(input("Enter no. of rounds you wanna play! : "))
round=1
won=0
lost=0
tie=0
while(round<=rounds):
    you=input("Enter what you chosse : ")
    r=random.randint(1,3)

    if r==1:
        com="r"
    elif r==2:
        com="p"
    elif r==3:
        com="s"

    
    i=["r","p","s"]
    if you in i:
        you=you
        print(f"You choose :{you}")
        print(f"com choose :{com}")
        a=game(com,you)

        if a==None:
            print("It's a tie!!!")
            tie+=1
        elif a==True:
            print("Congrat's you won!!!")
            won+=1
        elif a==False:
            print("Opps you lost!!!")
            lost+=1
        round+=1
        won=won
        lost=lost
        tie=tie
        
        
        
    else:
        print("wrong input")
        won=won
        lost=lost
        tie=tie
        round=round

print(f'''
    
    you won {won} 
    you lost {lost} 
    match tie {tie}  in {rounds} Rounds
    
    ''')

if won>lost:
    print("you won against computer")
elif won<lost:
    print("you lost aginst computer")
else:
    print("match is tie")
       
input("Enter any to exit: ")
        