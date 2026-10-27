# Lab 08 - Loops: while loop (Guess the Number)
#
# Pseudocode:
# - Jika pengguna belum menebak dengan benar, masuk ke loop.
# - Minta tebakan dari pengguna.
# - Apakah tebakan sama dengan angka?
# - Jika benar, beri tahu pengguna dan keluar dari loop.
# - Jika salah, beri tahu pengguna dan lanjutkan loop.

import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Angka acak antara 1 dan 10
number = random.randint(1, 10)

# Menandai apakah tebakan sudah benar
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
