import random
import art
import words

word_list = words.word_list
stages = art.stages
logo = art.logo
end_of_game = False
display = []
number_of_lives = 6

# generate a random word
chosen_word = random.choice(word_list)

# function to check if guessed letter is in chosen word
def check_function(chosen_word):
    position = 0
    for letter in chosen_word:
        if guess in chosen_word:
            return True
        else:
            return False

# function to replace blanks with correctly guessed letters
def replace_function():
    position = 0
    for letter in chosen_word:
        if guess == letter:
            display[position] = guess
        position += 1

print(logo)

# create blanks
for letter in chosen_word:
    display.append('_')
print(display)

# check game condition
while not end_of_game:
    guess = input("Guess a letter: ")
    
    # is the guessed letter in the word?
    if check_function(chosen_word):
        replace_function()
        print(display)
    else:
        # lose a life
        number_of_lives -= 1
        print(display)
        
        # have the run out of lives? 
        if number_of_lives == 0:
            end_of_game = True
            print("You lose")

    # are all the blanks filled?
    if "_" not in display:
        end_of_game = True
        print("You win")
    
    print(stages[number_of_lives])

    

