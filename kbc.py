import random

def game(i,flag,Ques_Set):
    ques=["Which of the following dynasties overthrew the Maurya dynasty to come to power around 73 BCE in Magadha?","'Agni Ki Udaan' is the Hindi translation of which personality’s autobiography?","Dadra, Nagar Haveli, Daman, and the island of Diu were all under which European colonial power?","The film featuring the song 'Teri Mitti' from Akshay Kumar starrer Kesari is based on which battle?","Which Indian hockey player holds the record for the most number of goals scored in an Olympic final?","In September 2020, which iconic motorcycle brand announced that it is shutting down its manufacturing facilities in India?","Which of these actresses once won a National Film Award for best female playback singer?","During the Battle of Kurukshetra, Krishna deceived the Kauravas by hiding the sun behind clouds to enable Arjuna to kill whom?","Who holds a national record with a timing of 50.79 seconds in women’s 400m track events?","In his retirement speech at Wankhede, who said, “My life between 22 yards for 24 years, it is hard to believe that this wonderful journey is coming to an end”?"]

    opt=[['A) Chera dynasty','B) Pala dynasty','C) Shunga dynasty','D) Kanva dynasty'],['A) Homi Jehagir Bhabha','B) Vikram Sarabhai', 'C) APJ Abdul Kalam','D) Kalpana Chawla'],['A) Denmark', 'B) Portugal', 'C) Britain' ,'D) France'],['A) Battle of Chamkaur', 'B) Battle of Saragarhi' , 'C) Battle of Buxar' ,'D) Battle of Plassey'],['A) Balbir Singh Senior','B) Leslie Claudius','C) Gurbux Singh','D) Keshav Dutt'],['A) Arctic Cat','B) Triumph','C) Indian','D) Harley Davidson'],['A) Neena Gupta','B) Deepika Chikhlia','C) Kirron Kher','D) Roopa Ganguly '],['A) Shakuni','B) Dushasana','C) Dronacharya','D) Jayadratha'],['A) Tintu Luka','B) Sunita Rani','C) Hima Das','D) Saraswati Saha'],['A) Anil Kumble','B) Sachin Tendulkar','C) Rahul Dravid','D) Gautam Gambhir']],

    ans=['D','C','B','B','A','D','D','D','C','B']
    if i>=len(prize):
        Rs=prize[len(prize)-1]
    else:
        Rs=prize[i]
    #to take random Question from list

    # To print question
    print(f"YOUR QUESTION FOR RS.{Rs} IS")
    print(ques[Ques_Set[i]])
    option=options(opt,i,Ques_Set)
    print(option)

    #To take answer from user
    a=input("CHOOSE ANY ONE ANSWER : ")
    a=a.capitalize() #TO match case

    #Game logic
    if a[0]==ans[Ques_Set[i]]:
        print("SAHI JABAB ")
    elif a[0]=='A' or a[0] == 'B'or a[0] == "C" or a[0] == "D":
        print("GALAT JABAB")
        flag=False
    else:
        print("CHUTIYA A ,B , C , D ma sa CHOOSE Karna hai")
        flag=False
    return flag

def future(flag):

    # Future of loop   
    con=input("Press Enter to Continue or any other key to Quit: ")
    if len(con)==0:
        print("Your Next Question is Followed")
        flag=True
        return flag
    else:
        print("Thanks for playing")
        flag=False
        return flag



# making option list to string
def options(opt,i,Ques_Set):
    str_opt=' '
    for item in opt[0][Ques_Set[i]]:
        str_opt+= str(item)+'\n'
    return str_opt.strip()
# making set of Question
def list_of_ques(count):
    Ques_set=[]
    while len(Ques_set)<count:
        num=random.randint(0,9)
        if num not in Ques_set:
            Ques_set.append(num)
    return Ques_set

print("WELCOME TO KBC")

flag=True
Ques_Set=list_of_ques(9)
prize=['50,000','1,00,000','20,00,000','40,00,000','80,00,000','1,00,00,000','3,00,00,000','5,00,00,000','7,00,00,000']
i=0
rs=0
while(flag):
    if len(Ques_Set)<=i or len(prize)<=i:
        if i==1:
            print("better luck next time")
        else:
            print(f"You won {prize[i-1]}")
        break
    flag=game(i,flag,Ques_Set)
    if i>=len(prize):
        Rs=prize[len(prize)-1]
    else:
        Rs=prize[i]
    if flag==True:
        flag=future(flag)
    if flag==False:
        rs=prize[i-1]
    i+=1
else:
    if i==1:
        print("better luck next time")
    else:
        rs=prize[i-2]
        print(f"You won {rs} he")




