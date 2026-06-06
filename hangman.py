import random

# List of 5 predefined words
words = ["apple", "tiger", "house", "robot", "music"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
wrong_guesses = 0

print("================================")
print("      WELCOME TO HANGMAN")
print("================================")

while wrong_guesses < max_attempts:

    # Display the word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed Letters:", guessed_letters)
    print("Attempts Left:", max_attempts - wrong_guesses)

    # Check win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")

# Lose condition
if wrong_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The word was:", word)

print("\nThank you for playing Hangman!")