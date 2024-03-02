import random
choose = input("What do you choose? Type 0  for Rock, 1 for Paper and 2 for Scissors: ")
computer = random.randint(0, 2)
if choose == "0" and computer == 0:
    print(f"Your choice {choose}")
    print(f"Computer choice {computer}")
    print("It's a draw")
elif choose == "0" and computer == 1:
    print(f"Your choice {choose}")
    print(f"Computer choice {computer}")
    print("You Won")
elif choose == "0" and computer == 2:
    print(f"Your choice {choose}")
    print(f"Computer choice {computer}")
    print("You Won")
elif choose == "1" and computer == 0:
    print(f"Your choice {choose}")
    print(f"Computer choice {computer}")
    print("You Lose")
elif choose == "1" and computer == 1:
    print(f"Your choice {choose}")
    print(f"Computer choice {computer}")
    print("It's a draw")
elif choose == "1" and computer == 2:
    print(f"Your choice {choose}")
    print(f"Computer choice {computer}")
    print("You Lose")
elif choose == "2" and computer == 0:
    print(f"Your choice {choose}")
    print(f"Computer choice {computer}")
    print("You Lose")
elif choose == "2" and computer == 1:
    print(f"Your choice {choose}")
    print(f"Computer choice {computer}")
    print("You Won")
elif choose == "2" and computer == 2: 
    print(f"Your choice {choose}")
    print(f"Computer choice {computer}")
    print("It's a draw")
else: 
    print(f"Your choice {choose}")
    print(f"Computer choice {computer}")
    print("Your input is out of range, choose numbers 0, 1 or 2")