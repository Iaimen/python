import random

from hangman import word_list
chosen_word=random.choice(word_list)
word_length=len(chosen_word)

end_of_game=False
lives=6

from hangman_logo import logo
print(logo)

display=[]
for _ in range(word_length):
    display+="_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess} that not in word. You loose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_logo import stages
    print(stages[lives])
