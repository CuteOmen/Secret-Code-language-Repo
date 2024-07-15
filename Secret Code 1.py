import random
import string


def generate_random_letters(length=3):
    return ''.join(random.choices(string.ascii_letters, k=length))


def encode_word(word):
    if len(word) <= 2:
        return word[::-1]
    elif len(word) > 3:
        word = word[1:] + word[0]
        word = word[::-1]
        prefix = generate_random_letters()
        suffix = generate_random_letters()
        return prefix + word + suffix


def decode_word(word):
    if len(word) <= 2:
        return word[::-1]
    elif len(word) > 6:  # Considering 3 random letters at both ends
        word = word[3:-3]
        word = word[::-1]
        return word[-1] + word[:-1]


def encode_message(message):
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)


def decode_message(message):
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)


def main():
    choice = int(
        input("Type 1 to create a secret message and type 2 for decoding: "))
    if choice == 1:
        message = input("Enter the message you want to encode: ")
        encoded_message = encode_message(message)
        print("Your encoded message is:", encoded_message)
    elif choice == 2:
        message = input("Enter the message you want to decode: ")
        decoded_message = decode_message(message)
        print("Your decoded message is:", decoded_message)
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
