import random
from hangman_words import word_list
from hangman_art import logo,stages

chosen_word = random.choice(word_list)

display = []

print(logo + "\n")

for letter in chosen_word:
    display.append("_")
# can also use display += "_"

print(display)

lives = 6


end_of_game = False

while not end_of_game:

    guess = input("Please guess a letter: ")

    guess.lower()

    word_length = len(chosen_word)

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed the letter {guess}. That's not in the word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose! The word was {chosen_word} :(")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win! :)")

    print(stages[lives])