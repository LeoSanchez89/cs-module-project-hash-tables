# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
from collections import Counter

frequency_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
decrypt_key = {}

def decipher_msg():
    with open("./applications/crack_caesar/ciphertext.txt") as f:
        c = Counter()
        doc = f.read()
        for char in doc:
            if char < 'A' or char > 'Z':
                pass
            else:
                c += Counter(char)
        c = dict(c)
        idx = 0
        sorted_dict = sorted(c, key=c.get, reverse=True)
        for i, value in enumerate(sorted_dict):
                decrypt_key[value] = frequency_list[idx]
                idx += 1
        decrypted_text = ""
        for char in doc:
            if char < 'A' or char > 'Z':
                decrypted_text += char
                continue
            decrypted_text += decrypt_key[char]
    return decrypted_text


print(decipher_msg())




