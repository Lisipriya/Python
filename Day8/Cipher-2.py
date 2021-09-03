alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  encode = ""
  for letter in plain_text:
    org_index = alphabet.index(letter)
    fin_index = org_index+ shift_amount
    if fin_index > 25:
      fin_index -=26
    fin_letter = alphabet[fin_index]
    encode = encode + fin_letter
  print(encode)
  

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(plain_text, shift_amount):
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
  decode = ""
  for letter in plain_text:
    org_index = alphabet.index(letter)
    fin_index = org_index - shift_amount
    if fin_index < 0:
      fin_index +=26
    fin_letter = alphabet[fin_index]
    decode = decode + fin_letter
  print(decode)

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
else:
  decrypt(plain_text=text, shift_amount=shift)