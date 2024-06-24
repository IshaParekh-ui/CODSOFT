import random


def display_hand_gesture(choice):
    if choice == 'rock':
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        """)
    elif choice == 'paper':
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
        """)
    elif choice == 'scissors':
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        """)


gestures = ["rock", "paper", "scissors"]
score = 0

def game_logic(users_choice, computers_choice):
    global score
    if users_choice == computers_choice:
        print("Its a tie!!")
    elif users_choice == "rock" and computers_choice == "paper" or users_choice == "paper" and computers_choice == "scissors" or users_choice == "scissors" and computers_choice == "rock":
        print("You loose. Better luck next time.")
    else:
        score += 1
        print("You win. Yayy!")


def play_game():
    users_choice = input("\nEnter your choice either rock, paper or scissors: ")
    if users_choice not in gestures:
        print("\nEnter a valid choice.")
        play_game()
    else:
        print(f"Your choice is {users_choice}.")
        display_hand_gesture(users_choice)

        computers_choice = random.choice(gestures)
        print(f"Computers choice is {computers_choice}.")
        display_hand_gesture(computers_choice)

        game_logic(users_choice, computers_choice)


game_on = True
while game_on:
    choice = input("Enter y to continue playing and n to quit: ").lower()
    if choice == "y":
        play_game()
    else:
        game_on = False
        print(f"Your score is {score}")
        print("Thanks for playing.")
