# from flask import Flask, render_template
# import base64
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     # Encode the message using base64
#     message = "Here we are, take this flag CTF_SDaT{best_cypto_flag}"
#     encoded_message = base64.b64encode(message.encode()).decode()
#
# # Encode base64 message using Caesar cipher
#     def caesar_cipher(text, shift):
#         result = ''
#         for char in text:
#             if char.isalpha():
#                 shifted = chr(((ord(char) - 65 + shift) % 26) + 65) \
#                     if char.isupper() else chr(((ord(char) - 97 + shift) % 26) + 97)
#                 result += shifted
#             else:
#                 result += char
#         return result
#
#     plaintext_message = "SGVyZSB3ZSBhcmUsIHRha2UgdGhpcyBmbGFnIENURl9TRGFUe2Jlc3RfY3lwdG9fZmxhZ30="
#     shift = 3
#     encoded_message_caesar = caesar_cipher(plaintext_message, shift)
#
#     # Render the output HTML page with encoded messages
#     return render_template('webpage.html',
#                            encoded_message=encoded_message, encoded_message_caesar=encoded_message_caesar)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('webpage.html')


if __name__ == '__main__':
    app.run(debug=True)
