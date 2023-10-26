from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(logo)


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift_amount) % 26
            end_text += alphabet[new_index]
        else:
            end_text += letter
    print(f"The {cipher_direction}d message is {end_text}")


again = "yes"

while again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(start_text=text, shift_amount=shift % 26, cipher_direction=direction)
    again = input("Type 'yes' if you want to go again.Otherwise type 'no'\n").lower()

print("GoodBye")