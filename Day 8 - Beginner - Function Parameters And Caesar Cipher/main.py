alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)


def caesar_cipher(initial_text, shift_p, direction_p):
  final_text = ""
  for char in initial_text:
    if char in alphabet:
      position = alphabet.index(char)
      if direction_p == "encode":
        new_position = position + shift_p
      elif direction_p == "decode":
        new_position = position - shift_p
      else:
        print("You have entered an invalid input")
        
    final_text += alphabet[new_position]

  print(f"The {direction_p}d text is {final_text}")


should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
  
    shift = shift % 25
    
    caesar_cipher(initial_text = text, shift_p = shift, direction_p = direction)
  
    decision = input("Type 'yes' if you wnant to continue, or 'no' if you want to exit\n")
    if decision == "no":
      should_continue = False

  else:
    print("You have entered an invalid input")
    should_continue = False
