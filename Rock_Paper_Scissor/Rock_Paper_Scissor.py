import random

print("Winning rules of the game ROCK PAPER SCISSORS are:\n"
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

# Initialize scores
user_score = 0
computer_score = 0
rounds = 5

for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}:")
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("Enter your choice: "))
    
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺: '))
    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    
    print('User  choice is:', choice_name)
    print("Now it's Computer's Turn...")
    
    comp_choice = random.randint(1, 3)
    
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)
    
    if choice == comp_choice:
        result = "DRAW"
        print("<== It's a tie! ==>")
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = 'Paper'
        computer_score += 1
        print("<== Computer wins! ==>")
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = 'Rock'
        user_score += 1
        print("<== User wins! ==>")
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        result = 'Scissors'
        user_score += 1
        print("<== User wins! ==>")

# Final score after 5 rounds
print("\nFinal Scores:") 
print("User  Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("<== User is the overall winner! ==>")
elif computer_score > user_score:
    print("<== Computer is the overall winner! ==>")
else:
    print("<== Overall result is a tie! ==>")

print("Thanks for playing!")
