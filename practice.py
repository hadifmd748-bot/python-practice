import random
print("Rock Paper Scissors Game")


choices = ["rock", "paper", "scissors"]


user = input("Enter rock, paper or scissors: ").lower()

computer = random.choice(choices)


print("Computer:", computer)


# Tie case

if user == computer:

    print("It's a Tie")


# Your winning cases

elif user == "rock" and computer == "scissors":

    print("You Win")


elif user == "paper" and computer == "rock":

    print("You Win")


elif user == "scissors" and computer == "paper":

    print("You Win")


# Computer winning cases

elif computer == "rock" and user == "scissors":

    print("Computer Wins")


elif computer == "paper" and user == "rock":

    print("Computer Wins")


elif computer == "scissors" and user == "paper":

    print("Computer Wins")


# Invalid input

else:

    print("Invalid Input")

