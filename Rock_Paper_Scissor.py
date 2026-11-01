# Python Mini Project : Rock Paper Scissor Game

"""
Working of Code

1. Input from the user : Rock, Paper, Scissor 
2. Computer Choice 
3. Result print

Cases : 
A. Rock 

Rock - Rock : Tie 
Rock - Paper : Paper win 
Rock - Scissor : Rock win

B . Paper 

Paper - Paper : Tie 
Paper - Rock : Paper Win
Paper - Scissor : Scissor Win 

C. Scissor 

Scissor - Scissor : Tie 
Scissor - Rock : Rock Win 
Scissor - Paper : Scissor Win 
"""

# Computer Vs User
# Importing random module so that computer pick the option randomly
import random

item=['rock','paper','scissor']

# Player Name
name=input("Enter your name: ")

# Logic of the game
flag=True
com_win=0
user_win=0
tie=0
while flag:
    # Choice by player and Computer

    player=input("Enter you move ( rock paper scissor) : ").lower()
    computer=random.choice(item)

    if player in item:
        print(f"{name} Choice: {player} \nComputer Choice : {computer}")

        if player==computer:
            print("The game is tie")
            tie+=1
        elif player=='rock':
            if computer=='paper':
                print('Computer wins.')
                com_win+=1
            else:
                print(f'{name} wins.')
                user_win+=1
        elif player =='scissor':
            if computer=='paper':
                print(f'{name} Wins')
                user_win+=1
            else: 
                print("Computer Wins")
                com_win+=1
        else: 
            if computer=='rock':
                print(f'{name} wins')
                user_win+=1
            else: 
                print('Computer wins.')
                com_win+=1

        ask=input("Do you want to play again (Yes/No): ").lower()
        if ask=='no':
            flag=False
    else:
        print(f"This is a wrong move.")  


# Score card

print("The final score: ")
print(f"Total round : {com_win+ user_win+tie} \nComputer : {com_win} \n{name} : {user_win} \nTie : {tie} ")
        

    