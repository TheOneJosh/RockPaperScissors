import random
import sys

print("Rock paper scissors!")


def choice():
    choice = input("Continue?(y/n): ")
    if choice != "n":
        ___int___()
    else:
        sys.exit()


def ___int___():
    while True:
        a = ("rock", "paper", "scissors")
        p1 = input("Enter your choice: ")
        p2 = random.choice(a)
        if p1 == p2:
            print("It's a draw!")
        elif p1 == "rock" and p2 == "paper":
            print("Computer wins! Computer picked paper.")
        elif p1 == "rock" and p2 == "scissors":
            print("You win! Computer picked scissors.")
        elif p1 == "paper" and p2 == "rock":
            print("You win! Computer picked rock.")
        elif p1 == "paper" and p2 == "scissors":
            print("Computer wins! Computer picked scissors.")
        elif p1 == "scissors" and p2 == "rock":
            print("Computer wins! Computer picked rock.")
        elif p1 == "scissors" and p2 == "paper":
            print("You win! Computer picked paper.")
        choice()
        continue
    return


___int___()
