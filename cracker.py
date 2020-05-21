import hashlib

password_hash = input('Enter hash: ')
wordlist = input('File name: ')

try:
    password_file = open(wordlist, 'r')
except:
    print('No File Found')
    quit()


for word in password_file:
    
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    if digest == password_hash:
        print('Password found')
        print('Password is ' + word)
        flag = 1
        break

if flag == 0:
    print('Password is not in the list')