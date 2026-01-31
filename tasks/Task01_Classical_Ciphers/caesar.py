def encryption(msg, key):
    ciphertext = ''
    for i in msg:
        if i in alphabet:
            ciphertext += alphabet[(alphabet.find(i) + key) % 26]
        else:
            ciphertext += i
    return ciphertext

def decryption(ciphertext, key):
    decrypted_text = ''
    for i in ciphertext:
        if i in alphabet:
            decrypted_text += alphabet[(alphabet.find(i) - key) % 26]
        else:
            decrypted_text += i
    return decrypted_text

from random import randint as rnd
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
msg = input("enter your message: ")
msg = msg.upper()
key = rnd(1,26)
encrpyted_msg = encryption(msg, key)
decrypted_msg = decryption(encrpyted_msg, key)

print("message: ", msg)
print("key: ", key)
print("encrypted message: ", encrpyted_msg)
print("decrypted message: ", decrypted_msg)
if decrypted_msg == msg:
    print("successfully decrypted!")
else:
    print("something went wrong!")