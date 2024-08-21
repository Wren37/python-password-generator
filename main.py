#password generator
import random
import string

def generatore_password(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation    #stores all characters in a variable to use
    password = ''.join(random.choice(alphabet) for i in range(length))      #randomly chooses out of the characters ten times (default length) to create a strong password
    return password

print(generatore_password())    #prints password to terminal
