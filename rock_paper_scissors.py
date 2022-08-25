from random import randint

choices = ["rock", "paper", "scissors"]
try_again = True
human_score = 0
computer_score = 0

while try_again:
    player_choice = input("enter your choice(rock/paper/scissors): ")
    correct_player_choice = player_choice in choices

    while not correct_player_choice:
        player_choice = input("wrong choice, enter rock/paper/scissors: ")
        correct_player_choice = player_choice in choices

    computer_choice = choices[randint(0, 2)]

    print("you choose: ", player_choice, " I choose: ", computer_choice)

    if player_choice == computer_choice:
        print("DRAW!!!")
    elif player_choice == "rock" and computer_choice == "paper":
        computer_score += 1
        print("Oh No!, You Lost!")
        print("your score is: ", human_score, " my score is: ", computer_score)
    elif player_choice == "rock" and computer_choice == "scissors":
        human_score += 1
        print("congrats!, you beat me!")
        print("your score is ", human_score, " my score is ", computer_score)
    elif player_choice == "paper" and computer_choice == "rock":
        human_score += 1
        print("congrats!, you beat me!")
        print("your score is: ", human_score, " my score is: ", computer_score)
    elif player_choice == "paper" and computer_choice == "scissors":
        computer_score += 1
        print("Oh No!, You Lost!")
        print("your score is: ", human_score, " my score is: ", computer_score)
    elif player_choice == "scissors" and computer_choice == "rock":
        computer_score += 1
        print("Oh No!, You Lost!")
        print("your score is: ", human_score, " my score is: ", computer_score)
    elif player_choice == "scissors" and computer_choice == "paper":
        human_score += 1
        print("congrats!, you beat me!")
        print("your score is: ", human_score, " my score is: ", computer_score)
    else:
        print("Error")

    try_again = bool(input("Try Again? (press enter to exit) "))
