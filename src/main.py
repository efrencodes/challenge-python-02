# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
LETTER_UPPERCASE = list(string.ascii_lowercase)
LETTER_LOWERCASE = list(string.ascii_uppercase)
NUMBERS = list(string.digits)
TYPES = ['SYMBOLS', 'LETTER_UPPERCASE', 'LETTER_LOWERCASE', 'NUMBERS']
MAX_NUMBER = 15
MIN_NUMBER = 7

def generate_password():
    random_number = random.randrange(MIN_NUMBER, MAX_NUMBER)
    password = ''
    for i in range(random_number):
        index = random.randrange(0,3)
        type = TYPES[index]

        if type == 'SYMBOLS':
            password +=  random.choice(SYMBOLS)
        elif  type == 'LETTER_UPPERCASE':
            password += random.choice(LETTER_UPPERCASE)
        elif  type == 'LETTER_LOWERCASE':
            password += random.choice(LETTER_LOWERCASE)
        elif  type == 'NUMBERS':
            password += random.choice(NUMBERS)

    return password

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
