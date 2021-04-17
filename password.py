import random, string

pw = ' '

def password(i):
    for j in range(i):
        pw += char(random.randint(0, 255))
    print(pw)