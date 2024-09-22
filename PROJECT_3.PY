#HANGMAN GAME 
#MINI_project in python
import random
import hangman_stages

word_list  = ['apple','mango','banana','hat','guvva','lion','tiger','fox','forest','cheetha','dog','strawberry','honey']
Chosen_word = random.choice(word_list)
print(Chosen_word)
show =[]
lives = 6 
game_over = False 

for  i in Chosen_word:
    show+="_"
print(show)
while not game_over:
    A = input("enter the gussed alphabet in the word :  ").lower()
    n = len(Chosen_word)
    #a = n-1
    for Position   in range(0,n ):
        letter = Chosen_word[Position]
        if letter == A :
            show[Position] = A
    
            
    if A not in Chosen_word:
        lives -=1
        if lives ==0:
            game_over = True
            print("you lose!!")
    if '_' not in show:
        game_over = True
        print("you win ")  
    print(show)    
    print(hangman_stages.stages[lives]) 
    


