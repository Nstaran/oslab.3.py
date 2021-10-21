import random
words_bank=['nastaran','open','linux','java','oslab','game','pen']
word=random.choice(words_bank)
john=9

user_true_chars=[]
while(True):
    win=1
    for char in word:
        
        if char in user_true_chars:
            print(char,end='')
            
        else:
            print('-',end='')
            win=0
            

    if (win==1):
            print(" \n you win")
              

    user_char=input("\n enter character: ")
    if user_char in word:
        user_true_chars.append(user_char)
        print('true')
        
       
    else:
        print('false')
        john-=1
        
        

    if(john==0):
        print("Game Over")

        break
