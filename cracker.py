import hashlib
import itertools
import time

def getPW(pw, stringType):
    start = time.time()
    char = stringType
    tries = 0

    for i in range(1, 9):
        for letter in itertools.product(char, repeat=i):
            tries += 1
            letter = ''.join(letter)
            if letter == pw:
                end = time.time()
                distance = end - start
                return (tries, distance)

password = input('Password: ')

string = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
attempts, timeAmount = getPW(password, string)
print('The cracker got the password %s in %s attempts and %s seconds.' % (password, attempts, timeAmount))
