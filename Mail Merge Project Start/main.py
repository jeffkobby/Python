# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

starting_letter = "Input/Letters/starting_letter.txt"
invited_names = "Input/Names/invited_names.txt"
PLACEHOLDER = "[name]"

# open name file and store each name in a list called "names"
with open(invited_names) as file:
    names = file.readlines()

with open(starting_letter) as file:
    content = file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
            completed_letter = file.write(new_letter)



