import hashlib

password_hash = input('Enter hash: ')
wordlist = input('File name: ')

try:
    password_file = open(wordlist, 'r')
except:
    print('No File Found')
    quit()



