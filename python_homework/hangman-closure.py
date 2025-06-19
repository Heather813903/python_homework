#Task 4

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter.lower())
        displayed = ''.join([ch if ch in guesses else '_' for ch in secret_word])
        print("Current word:", displayed)

        return all(ch in guesses for  ch in secret_word)
    
    return hangman_closure

if __name__ == "__main__":
    secret_word = input("Enter the secret  word: ").lower()
    print("\n" * 50)
    game = make_hangman(secret_word)

    print("Let's play Hangman!")
    guessed = False

    while not guessed:
        guess = input("Enter a letter ").lower()
        if len(guess) !=1 or not guess.isalpha():
            print("Enter a single alphabet letter")
            continue

        guessed = game(guess)

    print("Congratulations! You've guessed the word:", secret_word)

