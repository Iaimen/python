import random
import string

def encode(w):
    if len(w) >= 3:
        first_letter = w[0]
        w = w[1:] + first_letter
        random_chars = ''.join(random.choices(string.ascii_lowercase, k=3))
        return random_chars + w + random_chars
    else:
        return w[::-1]

def decode(code):
    if len(code) == 6:
        return code[::-1]
    else:
        random_chars = code[:3]
        last_letter = code[-1]
        return last_letter + code[3:-1]

w = input('Enter the word: ')
encoded_word = encode(w)
print("Encoded:", encoded_word)

decoded_word = decode(encoded_word)
print("Decoded:", decoded_word)
