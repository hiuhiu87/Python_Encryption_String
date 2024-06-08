import random
import string


def encrypt(text):
    """
    This function encrypts a given text using a simple substitution cipher.
    It generates a shuffled version of the character set and replaces each character in the input text with its corresponding character in the shuffled set.

    Args:
        text (str): The text to be encrypted.

    Returns:
        str: The encrypted text. If an error occurs during the process, it returns None.
    """
    try:
        chars = " " + string.ascii_letters + string.digits + string.punctuation
        chars = list(chars)
        keys = chars.copy()

        random.shuffle(keys)

        input_res = ""

        for letter in text:
            index = chars.index(letter)
            input_res += keys[index]

        return input_res
    except Exception as e:
        print(f"Error: {e}")
        return None


def decrypt(text):
    """
    This function decrypts a given text that was encrypted using the same substitution cipher as the encrypt function.
    It generates the same shuffled character set and replaces each character in the input text with its corresponding character in the original set.

    Args:
        text (str): The text to be decrypted.

    Returns:
        str: The decrypted text. If an error occurs during the process, it returns None.
    """
    try:
        chars = " " + string.ascii_letters + string.digits + string.punctuation
        chars = list(chars)
        keys = chars.copy()

        random.shuffle(keys)

        input_res = ""

        for letter in text:
            index = keys.index(letter)
            input_res += chars[index]

        return input_res
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    """
    This is the main execution point of the script.
    It encrypts a sample text, then decrypts it, and prints both the encrypted and decrypted versions.
    """
    res = encrypt("Hello, World!")
    res_de = decrypt(res)
    print(f"Encrypted: {res}")
    print(f"Decrypted: {res_de}")
