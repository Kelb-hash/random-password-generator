#list of object (alphanumeric "lower and uppercases")
#random
#range
#input
#for
#while
#entering the length of the password @e374reD
#enter how many password w= you must generate 2
#@e374reD
#@e374reD

import random

uppercase = "QWERTYUIOPLKJHGFDSAZXCVBNM"
lowercase = "qwertyuioplkjhgfdsazxcvbnm"
numbers = "1234567890"
symbols = "!@#$%&*()_+<;>.'[]"

all_seq = uppercase + lowercase + numbers + symbols

print(all_seq)

def password_gen():
    while 1:
        password_length = int(input("Enter password length: "))
        password_numbers = int(input("enter numbers of password"))
        for x in range(password_numbers):
            mypassword = ""
            for x in range(password_length):
                password_random = random.choice(all_seq)
                mypassword = mypassword + password_random
            print("hello password generated is: ", mypassword)
    quit()











                
                
password_gen()
