
#random
#range
#input
#for
#while

password_generator = "QWERTYUIOPLKJHGFDSAZXCVBNM1234567890#$@%&:mnbvcxzlkjhfgdsawer"
def passwordgenerator():
    while 1:
        #allow user to enter password length
        password_len = int(input("Enter password Length"))
        password_count = int(input("How many you to generate"))
        for x in range(0, password_count):
            mypass = ""


            for x in range(0, password_len):
                passwordmain = random.choice(passwordgenerator)
                mypass = mypassword + mypass
                print("hello this is my password", mypassword)

passwordgenerator()


x = 0

# while x < 6:
#     print(x)
#     x += 1