import random
print('hola mundo')

def create_pasword(pass_length):

    digits = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    pasword = ''

    for i in range(pass_length):

        pasword += random.choice(digits)

    print (pasword)

create_pasword(15)
