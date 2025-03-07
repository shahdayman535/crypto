import itertools


def decrypt_message(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    key_dict = dict(zip(key, alphabet))
    
    decrypted_text = ''.join([key_dict.get(char, char) for char in ciphertext.upper()])
    return decrypted_text


def generate_all_permutations():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return itertools.permutations(alphabet)


def brute_force_attack(ciphertext):
    
    all_permutations = generate_all_permutations()
    
    
    for idx, perm in enumerate(all_permutations):
        decrypted_text = decrypt_message(ciphertext, perm)
        print(f"Attempt {idx + 1}: {decrypted_text}")


ciphertext = input("Enter the encrypted message: ")


brute_force_attack(ciphertext)