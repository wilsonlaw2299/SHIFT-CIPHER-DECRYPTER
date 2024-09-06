def shift_encrypt(message, shift):
    encrypted_message = ""  # Initialize an empty string to store the encrypted message

    for char in message:
        if char.isalpha():  # Check if the character is an alphabet
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)  # Encrypt the character by shifting its Unicode value
            encrypted_message += encrypted_char  # Add the encrypted character to the encrypted message
        else:
            encrypted_message += char  # If the character is not an alphabet, add it to the encrypted message without encryption

    return encrypted_message  # Return the encrypted message


def shift_decrypt(message):
    decrypted_message = ""  # Initialize an empty string to store the decrypted message

    shift = find_most_common(message)  # Find the most common character in the encrypted message and determine the shift value

    for char in message:
        if char.isalpha():  # Check if the character is an alphabet
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)  # Decrypt the character by shifting its Unicode value
            decrypted_message += decrypted_char  # Add the decrypted character to the decrypted message
        else:
            decrypted_message += char  # If the character is not an alphabet, add it to the decrypted message without decryption

    return decrypted_message  # Return the decrypted message


def find_most_common(message):
    max_count = 0  # Initialize the maximum count of a character to 0
    freq_letter_array = []  # Initialize an empty array to store the most frequent characters

    # Iterate through each character in the message
    for char in message:
        if char.isalpha():  # Check if the character is an alphabet
            count = 0  # Initialize the count of the current character to 0
            # Count the occurrences of the current character in the message
            for char_moving in message:
                if char == char_moving:
                    count += 1

            if count >= max_count:  # If the count is greater than or equal to the maximum count
                if count > max_count:  # If the count is strictly greater than the maximum count
                    freq_letter_array.clear()  # Clear the array since there is a new character with a higher count
                max_count = count  # Update the maximum count
                freq_letter_array.append(char)  # Add the character to the array of most frequent characters

    final_array = []  # Initialize an empty array to store the final unique most frequent characters
    for char in freq_letter_array:
        if char not in final_array:  # If the character is not already in the final array
            final_array.append(char)  # Add the character to the final array

    if len(final_array) > 1:  # If there is more than one final most frequent character
        # Ask the user to select the most common character
        print(final_array)
        most_common = str(input("Select the most common char: "))
        while most_common not in final_array:  # Validate the user input
            most_common = str(input("Invalid input \nSelect the most common char: "))
    else:
        most_common = final_array[0]  # If there is only one final most frequent character, assign it directly

    shift_number = cal_shift_number(most_common)  # Calculate the shift number based on the most common character

    return shift_number  # Return the calculated shift number


def cal_shift_number(most_common):
    shift_number = (ord(most_common) - ord(default_common)) % 26  # Calculate the shift number based on the difference between the Unicode values of the most common character and the default common character
    return shift_number  # Return the calculated shift number

def read_file(file_path):
    """
    Read content from a file given the file path.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content read from the file.

    If the file is not found, print an error message and return an empty string.
    """
    try:
        # Attempt to open the file in read mode
        with open(file_path, 'r') as file:
            # Read and return the content of the file
            return file.read()
    except FileNotFoundError:
        # Handle the exception if the file is not found
        print("File not found. Please provide a valid file path.")
        return ""

def write_file(file_path, content):
    """
    Write content to a file at the specified file path.

    Args:
        file_path (str): The path to the file to be written to.
        content (str): The content to be written to the file.

    If successful, print a success message. If an error occurs, print the error message.
    """
    try:
        # Attempt to open the file in append mode
        with open(file_path, 'a') as file:
            # Append the content to the file with a newline character
            file.write(content + '\n')
        # Print a success message if the operation is successful
        print("File updated successfully.")
    except Exception as e:
        # Handle any exceptions that occur during the file writing process
        print("An error occurred while updating the file:", e)
    

base = ord('A')  # Base Unicode value for uppercase letters
default_long_text = 200  # Default minimum length for long text
default_common = "E"  # Default most common character

mode = int(input("Select mode by entering the number ONLY: \n[1]: Encrypt \n[2]: Decrypt \n[-1]: End\n"))
while mode != -1:
    if mode == 1:
        # For encryption mode
        input_choice = input("Choose input method: [1] Direct input [2] Read from file: ")
        
        # If direct input is chosen, get the message from user input
        # If reading from a file is chosen, prompt for the file path and read the message from the file
        if input_choice == '1':
            original_message = input("\nInput the string: ")
        elif input_choice == '2':
            file_path = input("Enter the file path: ")
            original_message = read_file(file_path)

        # Prompt for the shift value to encrypt the message
        shift = int(input("Shift number: "))
        
        # Encrypt the message using the shift value
        encrypted_message = shift_encrypt(original_message, shift)
        print("\nEncrypted Message: ", encrypted_message)

        # If reading from a file, append the original and encrypted messages to the file
        if input_choice == '2':
            write_file(file_path, f"Original Message: {original_message}\nEncrypted Message: {encrypted_message}")

    elif mode == 2:
        # For decryption mode
        input_choice = input("Choose input method: [1] Direct input [2] Use the same file: ")

        # If direct input is chosen, get the message from user input
        # If using the same file is chosen, prompt for the file path and read the message from the file
        if input_choice == '1':
            original_message = input("\nInput the string: ")
        elif input_choice == '2':
            file_path = input("Enter the file path: ")
            original_message = read_file(file_path)

        # Decrypt the message
        decrypted_message = shift_decrypt(original_message)
        print("\nDecrypted Message: ", decrypted_message)

        # If using the same file, append the original and decrypted messages to the file
        if input_choice == '2':
            write_file(file_path, f"Original Message: {original_message}\nDecrypted Message: {decrypted_message}")

    # Prompt the user to select the mode again for further operations or to end
    mode = int(input("\nSelect mode: \n[1]: Encrypt \n[2]: Decrypt \n[-1]: End "))