def generate_playfair_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is excluded
    keyword = "".join(dict.fromkeys(keyword.upper().replace("J", "I")))  # Remove duplicates and replace J with I
    matrix_key = keyword + "".join([char for char in alphabet if char not in keyword])

    # Create 5x5 matrix without numpy
    matrix = [list(matrix_key[i:i+5]) for i in range(0, 25, 5)]
    
    return matrix

def find_position(matrix, char):
    """Finds the position of a character in the Playfair matrix."""
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None  # If character is not found (shouldn't happen)

def format_text(plaintext):
    """Formats the text to be ready for Playfair encryption."""
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    formatted_text = ""
    
    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = plaintext[i+1] if i+1 < len(plaintext) else "X"

        if char1 == char2:  # No repeating letters in a pair
            formatted_text += char1 + "X"
            i += 1
        else:
            formatted_text += char1 + char2
            i += 2
    
    if len(formatted_text) % 2 != 0:  # If the length is odd, add 'X'
        formatted_text += "X"

    return formatted_text

def playfair_encrypt(plaintext, matrix):
    """Encrypts text using Playfair cipher rules."""
    plaintext = format_text(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle swap
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, matrix):
    """Decrypts text using Playfair cipher rules."""
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle swap
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    return plaintext

def main():
    keyword = input("Enter the keyword: ").strip()
    matrix = generate_playfair_matrix(keyword)
    
    print("\nPlayfair Matrix:")
    for row in matrix:
        print(" ".join(row))

    choice = input("\nChoose (E)ncrypt or (D)ecrypt: ").strip().lower()
    
    if choice == "e":
        plaintext = input("Enter the plaintext: ").strip()
        encrypted_text = playfair_encrypt(plaintext, matrix)
        print("\nEncrypted Text:", encrypted_text)
    elif choice == "d":
        ciphertext = input("Enter the ciphertext: ").strip()
        decrypted_text = playfair_decrypt(ciphertext, matrix)
        print("\nDecrypted Text:", decrypted_text)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()