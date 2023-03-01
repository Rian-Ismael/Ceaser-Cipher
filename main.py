alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #25 (não conta com 0)

def caesar(text, shift, direction):
    end_text = ""
    for letter in range(len(text)):
        if direction == "encode":
            if not text[letter] in alphabet:
                end_text += text[letter]
            else:
                aux = alphabet[(alphabet.index(text[letter])) + shift]
                end_text += aux
                            
        elif direction == "decode":
            if not text[letter] in alphabet:
                end_text += text[letter]
            else:
                shift = shift % 26
                aux = alphabet[(alphabet.index(text[letter]) - shift)]
                end_text += aux          

    print(f"The {direction} text is <{end_text}>")


from art import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

while True:
    caesar(text, shift, direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if again == "no":
        print("Goodbye")
        break

    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        