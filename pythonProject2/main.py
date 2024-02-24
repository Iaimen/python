alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser(start_text,shift_number,directions):
    end_text = ""
    if directions == "decode":
        shift_number *= -1
    for char in start_text:
        if char in alphabet:
           position = alphabet.index(char)
           new_position = position+shift_number
           end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {directions}d result:  {end_text}")
from logo import logos
print(logos)
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type a message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceaser(start_text=text, shift_number=shift, directions=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
     should_end = True
     print("Goodbye")