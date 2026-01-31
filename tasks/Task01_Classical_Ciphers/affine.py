def encryption(msg, a, b):
    ciphertext = ''
    for i in msg:
        if i in alphabet:
            ciphertext += alphabet[((alphabet.find(i) * a) + b) % 26]
        else:
            ciphertext += i
    return ciphertext

def inverse(n):
    for i in range (1, 26):
        if (n * i) % 26 == 1:
            return i

def decryption(ciphertext, a, b):
    decrypted_msg = ''
    for i in ciphertext:
        if i in alphabet:
            decrypted_msg += alphabet[(inverse(a) * (alphabet.find(i) - b)) % 26]
        else:
            decrypted_msg += i
    return decrypted_msg


from random import randint as rnd
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
msg = input("enter your message: ")
msg = msg.upper()
a_values = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
a = a_values[rnd(0,10)]
b = rnd(0,26)

print("message: ", msg)
print(f"keys: a = {a}; b = {b}")
encrypted_msg = encryption(msg, a, b)
print("encrypted message: ", encrypted_msg)
decrypted_msg = decryption(encrypted_msg, a, b)
print("decrypted message: ", decrypted_msg)
if decrypted_msg == msg:
    print("successfully decrypted!")
else:
    print("something went wrong!")