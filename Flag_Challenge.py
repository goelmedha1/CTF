import base64

#Encode the message using base64
message = "Here we are, take this flag CTF{best_cypto_flag}"
encoded_message = base64.b64encode(message.encode()).decode()
print("Encoded Message:", encoded_message)


#Encode base64 message using ceasar cipher
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + shift) % 26) + 97)
            result += shifted
        else:
            result += char
    return result

# Encoded base64 message
plaintext_message = "SGVyZSB3ZSBhcmUsIHRha2UgdGhpcyBmbGFnIENURntiZXN0X2N5cHRvX2ZsYWd9"

# Choose a shift value for the Caesar cipher
shift = 3

# Apply Caesar cipher
encoded_message_caesar = caesar_cipher(plaintext_message, shift)
print("Encoded message using Caesar cipher:", encoded_message_caesar)


#Decode ceasar cipher message
def caesar_cipher_decrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = chr(((ord(char) - 65 - shift) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 - shift) % 26) + 97)
            result += shifted
        else:
            result += char
    return result

# Encoded message using Caesar cipher
encoded_message_caesar = "VJYbCVE3CVEkfpXvLKUkd2XjgJksfbEpeJIqLHQXUqwlCAQ0A2Q5fKUyA2CvBZg9"

# Choose the same shift value used for encryption
shift = 3

# Decrypt the message using the Caesar cipher
decoded_message_caesar = caesar_cipher_decrypt(encoded_message_caesar, shift)
print("Decoded message using Caesar cipher:", decoded_message_caesar)


#Decrypt the ceaser message using base64
decoded_message = base64.b64decode(decoded_message_caesar.encode()).decode()
print("Decoded Message:", decoded_message)

