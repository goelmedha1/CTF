import base64

#Encode the message using base64
message = "Congratulations! You found the flag: CTF_SDaT{H3r3s_Your_Fl4g_Cryp70_M45t3rm1nd}"
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
plaintext_message = "Q29uZ3JhdHVsYXRpb25zISBZb3UgZm91bmQgdGhlIGZsYWc6IENURl9TRGFUe0gzcjNzX1lvdXJfRmw0Z19DcnlwNzBfTTQ1dDNybTFuZH0="

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
encoded_message_caesar = "T29xC3MkgKYvBAUse25cLVECe3XjCp91epTjgJkoLJCvBZf6LHQXUo9WUJIXh0jcfmQcA1oygAMiUpz0C19GfqozQcEiWWT1gGQbeWIxCK0="

# Choose the same shift value used for encryption
shift = 3

# Decrypt the message using the Caesar cipher
decoded_message_caesar = caesar_cipher_decrypt(encoded_message_caesar, shift)
print("Decoded message using Caesar cipher:", decoded_message_caesar)


#Decrypt the ceaser message using base64
decoded_message = base64.b64decode(decoded_message_caesar.encode()).decode()
print("Decoded Message:", decoded_message)

