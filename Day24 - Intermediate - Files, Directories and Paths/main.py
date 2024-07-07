CHANGED_TEXT = "[name]"

with open("Input/Names/invited_names.txt") as name_file:
    invited_names = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

for name in invited_names:
    striped_name = name.strip()
    updated_letter = letter.replace(CHANGED_TEXT, striped_name)
    with open(f"Output/ReadyToSend/letter_for_{striped_name}.txt", mode= "w") as store_letter:
        store_letter.write(updated_letter)
