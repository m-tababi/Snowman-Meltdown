import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    final_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            final_word += letter + " "
        else:
            final_word += "_ "
    print("Word: ", final_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        # Check for empty input
        if guess == "":
            print("Please enter a letter.\n")
            continue

        # Check for multiple letters
        if len(guess) > 1:
            print("Please guess only one letter.\n")
            continue

        # Check for repeated guess
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        # Check if input is a letter
        if not guess.isalpha():
            print("Please use letters only.\n")
            continue

        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print("Good guess!\n")
        else:
            print("Wrong guess!\n")
            mistakes += 1

        # Check if player lost
        if mistakes >= 3:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Game Over! The word was:", secret_word)
            break

        # Check if player won
        all_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_guessed = False
                break

        if all_guessed:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations! You guessed the word:", secret_word)
            break

    # Ask if the player wants to play again
    while True:
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay == "yes":
            print("\nStarting a new game...\n")
            play_game()  # Start again
            break
        elif replay == "no":
            print("Thanks for playing! Goodbye")
            break
        else:
            print("Please enter 'yes' or 'no'.")
