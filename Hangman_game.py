import random

# Predefined words
intializing_words = ["computer", "mouse", "keyboard", "display", "screen"]

# Choose random word
word = random.choice(intializing_words)
word_letters = list(word)

# Game state
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Hangman game!")
print(f"You have {max_wrong} wrong guesses allowed.\n")

# Game loop
while wrong_guesses < max_wrong:
    # Display progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display.strip())

    # Check win
    if all(letter in guessed_letters for letter in word):
        print("\nYou won! The word was:", word)
        break

    # User input
    guess = input("\nGuess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter only.")
        continue

    if guess in guessed_letters:
        print("Already guessed.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print(f"Wrong! {max_wrong - wrong_guesses} guesses left.")

    print()

else:
    print("Game Over! The word was:", word)