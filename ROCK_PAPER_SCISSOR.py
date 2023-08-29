# ROCK, PAPER & SCISSOR

import random
a=["rock", "paper", "scissor"]
b=int(input('What\'s your choice ("0 for rock", "1 for paper", "2 for scissor"):'))
comp_choice=random.randint(0,2)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print(f"Computer choose: {a[comp_choice]}")
if comp_choice==0 :
    
    print(rock)
elif comp_choice==1:
    print(paper)
elif comp_choice==2:
    print(scissors)

if b==0 :
    print("You choose rock")
    print(rock)
elif b==1:
    print("You choose paper")
    print(paper)
elif b==2:
    print("You choose scissor")
    print(scissors)
else :
    print("Wrong Input")
      
if comp_choice==b:
    print("DRAW")
elif comp_choice==0 and b==2:
    print("You Lose")
elif comp_choice==0 and b==1:
    print("You Win")
elif comp_choice==1 and b==2:
    print("You Win")
elif comp_choice==1 and b==0:
    print("You lose")
elif comp_choice==2 and b==0:
    print("You win")
elif comp_choice== 2 and b==1:
    print("You lose")
else:
    print("Wrong Input")
