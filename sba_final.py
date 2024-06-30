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


base = ord('A')  # Base Unicode value for uppercase letters
default_long_text = 200  # Default minimum length for long text
default_common = "E"  # Default most common character

mode = int(input("Select mode by entering the number ONLY: \n[1]: Encrypt \n[2]: Decrypt \n[-1]: End\n"))
while mode != -1:

    check_upper = False

    while not check_upper:
        original_message = str(input("\nInput the string: "))
        check_upper = True

        for char in original_message:
            if char.isalpha():
                if char.islower():
                    check_upper = False
                    break

        if not check_upper:
            print("The character(s) is not in all uppercase")
            opt_invalid_input = str(input("Enter the letter: \n[R]: Enter the string again \n[U]: Convert all character(s) into uppercase \n"))

            if opt_invalid_input == "U":
                original_message = original_message.upper()  # Convert all characters to uppercase

    if mode == 1:
        shift = int(input("Shift number: ")) 
        print("\nEncrypted Message: ", shift_encrypt(original_message, shift))

    elif mode == 2:
        if len(original_message.split(" ")) < default_long_text: 
            if str(input("The message is not long enough (>200 words), \nThe result may be inaccurate. \nContinue[Y/N]")) == "Y":
                print("\nDecrypted Message: ", shift_decrypt(original_message))
        else:
            print("\nDecrypted Message: ", shift_decrypt(original_message))

    mode = int(input("\nSelect mode: \n[1]: Encrypt \n[2]: Decrypt \n[-1]: End "))