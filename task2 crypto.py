import string
from collections import Counter


ciphertext = "qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald"


alphabet = string.ascii_lowercase

letter_frequencies = Counter(ciphertext.replace(" ", ""))  


sorted_cipher_freqs = sorted(letter_frequencies.items(), key=lambda x: x[1], reverse=True)


english_letter_freq = "etaoinshrdlcumwfgypbvkjxqz"


cipher_letter_order = [pair[0] for pair in sorted_cipher_freqs]
decryption_map = {cipher_letter_order[i]: english_letter_freq[i] for i in range(len(cipher_letter_order))}


def decrypt_with_frequency_analysis(ciphertext, mapping):
    decrypted_text = ""
    for char in ciphertext:
        if char in mapping:
            decrypted_text += mapping[char]
        else:
            decrypted_text += char  
            return decrypted_text


decrypted_text = decrypt_with_frequency_analysis(ciphertext, decryption_map)


print("Letter Frequencies in Ciphertext:", sorted_cipher_freqs)
print("Decryption Mapping:", decryption_map)
print("\nDecrypted Text (Using Frequency Analysis):")
print(decrypted_text)