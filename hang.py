import random

def hangman_game():
    # List of words to choose from
    words = ['python', 'hangman', 'programming', 'challenge', 'developer']
    word = random.choice(words).lower()  # Randomly select a word
    guessed_word = ['_'] * len(word)  # Initialize the word display with underscores
    guessed_letters = set()  # Track guessed letters
    max_attempts = 6  # Limit on incorrect guesses
    attempts = 0  # Counter for incorrect guesses

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {max_attempts} incorrect guesses allowed.\n")
    
    # Main game loop
    while attempts < max_attempts:
        print("Word:", ' '.join(guessed_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Remaining attempts: {max_attempts - attempts}")

        # Player input
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Wrong guess! '{guess}' is not in the word.\n")
            attempts += 1

        # Check if the player has won
        if '_' not in guessed_word:
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print(f"Game over! The word was: {word}")

# Run the game
hangman_game()