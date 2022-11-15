from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      end_text += char
    else:
      position = alphabet.index(char)
      if (position + shift_amount) > 25: 
        new_position = (position + shift_amount) % 26
        end_text += alphabet[new_position]
      else:
        new_position = position + shift_amount
        end_text += alphabet[new_position]  
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  cycle = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
  if cycle.lower() == 'no':
    break 