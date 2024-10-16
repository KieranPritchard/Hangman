import random

words = ["Python", "Java", "JavaScript", "Ruby"]
word = random.choice(words).lower()
guessed_letters = []

def header():
    print('-' * 30)
    print("Hangman Game")
    print('-' * 30)

def display_word():
    display = ''
    for char in word:
        if char in guessed_letters:
            display += char
        else:
            display += "_"
    print(display)
    return display

def main():
    trys = 10
    while trys > 0:
        header()
        display = display_word()

        user_input = input("Please Input Character: ").lower()

        if user_input in word and user_input not in guessed_letters:
            guessed_letters.append(user_input)
        elif user_input not in word:
            trys -= 1
            print(f"Incorrect! You have {trys} tries left.")
        else:
            print("You already guessed that letter.")

        if display == word:
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print("Game over! The word was:", word)

if __name__ == "__main__":
    main()
