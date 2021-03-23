import random


class GoodPasswordsGenerator:
    """
    Good paswords generator
    """
    def __init__(self):
        self.alphabet = '1234567890' \
                        'qwertyuiopasdfghjklzxcvbnm' \
                        'QWERTYUIOPASDFGHJKLZXCVBNM' \
                        '!@#$%^&*()_+{}:"|<>?'

    def next(self, lenght=10):
        password = ''
        for i in range(lenght):
            c = random.choice(self.alphabet)
            password += c
        return password


user_input = int(input('My password will contain this many symbols: '))

generator = GoodPasswordsGenerator()
print(generator.next(user_input))