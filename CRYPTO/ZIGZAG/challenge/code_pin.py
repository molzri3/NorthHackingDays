import random
import string
from hidden.hidden import FLAG,PIN
key1 = int(str(PIN)[:2])
key2 = int(str(PIN)[2:])



def encrypt(plaintext,key):
    plaintext = "".join(plaintext.split())
    r = [['pin' for i in range(len(plaintext))] 
         for j in range(key)]

    down = False
    col = 0
    row = 0
    for i in range(len(plaintext)):
        if(row == 0) or (row == key-1):
            down = not down
        r[row][col] = plaintext[i]
        col += 1
        if down:
            row +=1
        else:
            row -=1    
    ciphertext = []
    for i in range(key):
        for j in range(len(plaintext)):
            if r[i][j] != 'pin':
                ciphertext.append(r[i][j])
    return "".join(ciphertext)



def expand_string(original,key) -> str:
    random.seed(key)  
    expanded = []
    first_random_char = random.choice(string.ascii_letters + string.digits + string.punctuation)
    expanded.append(first_random_char)

    for char in original:
        expanded.append(char)
        for _ in range(9):
            random_char = random.choice(string.ascii_letters + string.digits + string.punctuation)
            expanded.append(random_char)

    return ''.join(expanded)

if __name__=='__main__':
    first  = encrypt(FLAG,key1)
    second = expand_string(first,key2)
    with open('out.txt','+w') as out:
        out.write("the cipher is : "+second)
