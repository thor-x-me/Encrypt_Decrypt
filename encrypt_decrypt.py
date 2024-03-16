secrets = {'a': '~', 'b': '+', 'c': 't', 'd': ')', 'e': '5', 'f': ';', 'g': '1', 'h': '&', 'i': 'c',
           'j': '8', 'k': '-', 'l': 'a', 'm': '[', 'n': '?', 'o': ' ', 'p': 'b', 'q': 'g', 'r': '<',
           's': 'm', 't': 'e', 'u': '7', 'v': 'd', 'w': 'v', 'x': 'f', 'y': 'i', 'z': '{', ' ': 'l',
           '0': 'u', '1': 'j', '2': '>', '3': 'k', '4': 'o', '5': '/', '6': 'w', '7': '6', '8': 'p',
           '9': '_', '`': '4', '~': '2', '!': '|', '@': ':', '#': 'n', '$': 'r', '%': 'z', '^': ',',
           '&': 's', '*': '=', '(': '0', ')': 'x', '_': '.', '+': 'y', '-': 'h', '=': 'q', '[': '3',
           '{': '9', ']': '`', '}': '!', '|': '@', ';': '#', ':': '$', ',': '%', '.': '^', '/': '*',
           '?': '(', '<': ']', '>': '}'}
secrets_dec = {'~': 'a', '+': 'b', 't': 'c', ')': 'd', '5': 'e', ';': 'f', '1': 'g', '&': 'h', 'c': 'i',
               '8': 'j', '-': 'k', 'a': 'l', '[': 'm', '?': 'n', ' ': 'o', 'b': 'p', 'g': 'q', '<': 'r',
               'm': 's', 'e': 't', '7': 'u', 'd': 'v', 'v': 'w', 'f': 'x', 'i': 'y', '{': 'z', 'l': ' ',
               'u': '0', 'j': '1', '>': '2', 'k': '3', 'o': '4', '/': '5', 'w': '6', '6': '7', 'p': '8',
               '_': '9', '4': '`', '2': '~', '|': '!', ':': '@', 'n': '#', 'r': '$', 'z': '%', ',': '^',
               's': '&', '=': '*', '0': '(', 'x': ')', '.': '_', 'y': '+', 'h': '-', 'q': '=', '3': '[',
               '9': '{', '`': ']', '!': '}', '@': '|', '#': ';', '$': ':', '%': ',', '^': '.', '*': '/',
               '(': '?', ']': '<', '}': '>'}


def encrypt(simple):
    enc = ''
    for i in simple:
        i = i.lower()
        enc = enc + secrets.get(i)
    return enc

def decrypt(simple):
    enc = ''
    for i in simple:
        enc += secrets_dec.get(i)
    return enc


def enc_layer(pswd: str, layer: int = 0):
    ps = pswd
    for i in range(layer):
        ps = encrypt(ps)
    return ps


def dec_layer(pswd: str, layer: int = 0):
    ps = pswd
    for i in range(layer):
        ps = decrypt(ps)
    return ps


def run():
    print("""
    - TO ENCRYPT YOUR MESSAGE ENTER 1
    - TO DECRYPT YOUR MESSAGE ENTER 2
    - TO CLOSE THE PROGRAM ENTER 3""")
    choice = input("Enter your choice: ")
    if choice == '1':
        message = input("Enter your message: ")
        password = int(input("Enter your password of 6 digits(0-9): "))
        assert len(str(password)) == 6, "Password"
        encrypted_message = enc_layer(message, password)
        print(f"Your encrypted message is: \n{encrypted_message}")
        run()
    elif choice == '2':
        message = input("Enter your encrypted message: ")
        password = int(input("Enter your password of 6 digits(0-9): "))
        assert len(str(password)) == 6, "Password"
        decrypted_message = dec_layer(message, password)
        print(f"Your decrypted message is: \n{decrypted_message}")
        run()
    elif choice == '3':
        exit()
    else:
        print("Wrong choice.")
        run()


if __name__ == '__main__':
    print("""
        ###############################################################
        WELCOME TO ENCRYPTER-DECRYPTER PROGRAM
        THIS PROGRAM IS MADE BY THOR_X_ME
        """)
    run()
