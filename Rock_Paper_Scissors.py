import random
#slection of computer
list=["rock","paper","scissors"]
computer_select=random.choice(list)

#input for user
user_selection=input('enter your choice "rock", "paper", "scissors" \n')

if user_selection=="rock" :
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif user_selection=="paper" :
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif user_selection=="scissor" :
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

print("computer choice:",computer_select)


if computer_select=="rock" :
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif computer_select=="paper" :
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif user_selection=="scissor" :
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if user_selection==computer_select:
    print("tie")
elif user_selection=="rock" and computer_select==("scissors"):

    print("you win")
elif user_selection=="scissor" and computer_select==("paper"):

    print("you win")
elif user_selection=="paper" and computer_select==("rock"):

    print("you win")
else:

    print("you lose")
