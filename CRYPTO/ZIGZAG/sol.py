from hidden.hidden import FLAG, PIN
import random
key1 = int(str(PIN)[:2])
key2 = int(str(PIN)[2:])


cipher = """eNK`s7V\`m6H/":c$3,V<D)3YwhnpWt{mu$"qX/#IZ,xWig-hxhIvLJj%<n-@G@]hm<6?}Q_Q&\`4vqkOZg.IV~x]:jA)[oM"~U|3Gf81:kTq?l_\~t,Nn_'204.esanpqc0Rp|'"H`6R0Xl|el|A]Z0y^,ZH/.0P_YSgx'wy{gC\DMCSyBXXHCh6#hmdd(4;$##o-SHCLq5YtFan`CLp+<1zW2nbExWoQOH'r(N,t_FzEflIG9`I?j9{RsEOCb~A8>tK_+\4M}94N)}!);2}3%,j"""
def decrypt(ciphertext , key):
    rail = [['*' for i in range(len(ciphertext))] for j in range(key)]
    down = None
    col = 0
    row = 0 
    for i in range(len(ciphertext)):
        if row == 0:
            down = True
        if row == key - 1: 
            down = False

        rail[row][col] = 'mkr'
        col += 1
        
        if down :
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if ((rail[i][j]=='mkr') and (index < len(ciphertext))):
                rail[i][j] = ciphertext[index]
                index += 1 
    
    plaintext = []
    col = 0
    row = 0

    for i in range(len(ciphertext)):
        if row == 0:
            down = True
        if row == key - 1:
            down = False
        
        plaintext.append(rail[row][col])
        col +=1 

        if down:
            row +=1
        else:
            row -=1
    
    return "".join(plaintext)




def reverse_expand_string(expanded,key) -> str:
    random.seed(key)  
    original = []
    i = 1
    while i < len(expanded):
        original.append(expanded[i])
        i += 1
        i += 9
    return ''.join(original)


print(decrypt(reverse_expand_string(cipher,key2),key1))




