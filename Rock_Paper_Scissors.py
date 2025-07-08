import os
import random

round_number = 1
options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
ties = 0

print("=== Rock, Paper, Scissors ===")

while True:
    print(f"\n--- Round {round_number} ---")
    round_number += 1
    user_choice = input("Enter your choice (rock/paper/scissors or 'q' to quit): ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    if user_choice == 'q':
        print("\nFinal Score:")
        print(f"You won {user_score} time(s)")
        print(f"Computer won {computer_score} time(s)")
        print(f"Ties: {ties}")
        print("Thanks for playing!")
        break

    if user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(options)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1