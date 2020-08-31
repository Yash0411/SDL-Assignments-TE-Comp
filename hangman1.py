import random

# Enter Name
name = input("What is your name? ")
print("Good Luck!",name)

words=["computer","cpu","monitor","mouse","laptop","keyboard","printer","scanner","pendrive","drive","floopy"]
print("Given Words Are :",words)

# Declare chances
chances = 12

# Choose a word ar=t random
word = random.choice(words)
letters = []

# Play
for i in range(chances):
    letters = []
    for j in range(len(word)):
        # Input a character
        c = input("Guess a character : ")
        
        # Check character conditions

        # Condition 1 Character not in word
        if c not in word:
            print("\n Missed it... \n Chance",i+1,"ended\n")
            break

        # Condition 2 Character in word added more than count
        elif word.count(c) <= letters.count(c):
            print("\n Missed it... \n Chanced",i+1,"ended\n")
            break
        
        # Perfect condition
        else:
            letters.append(c)
    
    # Check correct or not
    if sorted(word) == sorted(letters) :
        print("You Won\n Guessed Word is",word,"!")
        break
    
    # Check whether chances have been ended
    if i==11:
        print("Haanged !!!\nYou lost better luck next time......")
           
    

