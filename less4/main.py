# **1.** Return uncommon elements of lists. Order of elements does not matter.

# input:
#     list1 = [1, 1, 2]
#     list2 = [2, 3, 4]
# output: [1, 1, 3, 4]

# input:
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
# output: [1, 2, 3, 4, 5, 6]

# input:
#     list1 = [1, 1, 2, 3, 4, 2]
#     list2 = [1, 3, 4, 5]
# output: [2, 2, 5]

list1 = [1, 1, 2]
list2 = [2, 3, 4]
res_arr = []
for i in list1:
    if i not in list2:
        res_arr.append(i)
    
for i in list2:
    if i not in list1:
        res_arr.append(i)

print(res_arr)


# **2.** Print the square of each number which is less than `n` on a separate line.

# input: n = 5
# output:
#     1
#     4
#     9
#     16

n = 5
for i in range(1, n):
    print(i**2)

# **3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.


# input: hello
# output: hel_lo

# input: assalom
# output: ass_alom

# input: abcabcdabcdeabcdefabcdefg
# output: abc_abcd_abcdeab_cdef_abcdefg

# incorrect task


# **4. Number Guessing Game**

# Create a simple number guessing game.
# - The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.

# > Hint: Use Python’s `random.randint()` to generate the number.

from random import randint

a = randint(1, 100)
steps = 0


while(True):
    guess = int(input("Enter your guess: "))
    steps += 1
    if steps == 10:
        print("You lost. Want to play again? ")
        ans = input()
        if ans not in ['Y', 'YES', 'y', 'yes', 'ok']:
            break
        else:
            a = randint(1, 100)
            steps = 0
    if guess > a:
        print("Too high!")
    elif guess < a:
        print("Too low!")
    else:
        print("You guessed it right!")
        ans = input("Want to play again?: ")
        if ans not in ['Y', 'YES', 'y', 'yes', 'ok']:
            break
        else:
            a = randint(1, 100)
            steps = 0


# **5. Password Checker**
# Task: Create a simple password checker.
# - Ask the user to enter a password. 
# - If the password is shorter than 8 characters, print "Password is too short." 
# - If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
# - If the password meets both criteria, print "Password is strong."

a = input("Enter a password: ")
if len(a) < 8:
    print("Password is too short.")
elif not any(c.isupper() for c in a):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")

# **6. Prime Numbers**
# Task: Write a Python program that prints all prime numbers between 1 and 100.

# > A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.

for i in range(2, 101):
    isPrime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)


# ---

# ### Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
# - The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
# - The player enters their choice.
# - Display the winner and keep track of scores for the player and the computer.
# - First to 5 points wins the match.

def player_status(p, c):
    if p == c: return 0;
    elif (p == 'rock' and c == 'scissors') or (p == 'paper' and c == 'rock') or (p == 'scissors' and c == 'paper'):
        return 1;
    else: return -1;

from random import choice
options = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

while True:
    if max(player_score, computer_score) == 5:
        if player_score > computer_score:
            print("Congratulations! You won the match!")
        else:
            print("Computer won the match! Better luck next time.")
        break
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    computer_choice = choice(options)
    print(f"Computer chose: {computer_choice}")
    
    result = player_status(player_choice, computer_choice)
    if result == 1:
        print("You win this round!")
        player_score += 1
    elif result == -1:
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")
    
    print(f"Scores => Player: {player_score}, Computer: {computer_score}")
