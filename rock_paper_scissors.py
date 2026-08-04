import random

print("--- rock, paper, scissors game ---")
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
print(f"Aapne chuna: {user_choice}")
print(f"Computer ne chuna: {computer_choice}")

if user_choice == computer_choice:
    print("Match Tie ho gaya! 🤝")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Aap Jeet Gaye! 🎉")
    else:
        print("Computer Jeet Gaya! 🤖")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Aap Jeet Gaye! 🎉")
    else:
        print("Computer Jeet Gaya! 🤖")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Aap Jeet Gaye! 🎉")
    else:
        print("Computer Jeet Gaya! 🤖")
else:
    print("Invalid input! rock, paper, ya scissors likhein.")

