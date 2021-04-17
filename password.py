import random, string

def password(i):
    pw = ""
    for _ in range(i):
        pw += chr(random.randint(32, 126))
    print(pw)
    
userIn = input("Length of password: ")
userIn = int(userIn)
password(userIn)