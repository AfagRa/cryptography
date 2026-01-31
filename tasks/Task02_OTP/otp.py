def str_to_unicode(msg):
    unicode_symbols = []
    for i in range (len(msg)):
        unicode_symbols.append(ord(msg[i]))
    return unicode_symbols

def unicode_to_binary(unicode_arr):
    binary_symbols = []
    for num in unicode_arr:
        binary = ''
        while num > 0:
            r = num % 2
            binary += str(r)
            num //=2
        binary += '0' * (8 - len(binary))
        binary_symbols += binary[::-1]
    return "".join(binary_symbols)

from random import randint as rnd
def key_generator(length):
    key = ''
    for i in range (length):
        key += str(rnd(0,1))
    return key

def encryption(binary_msg, key):
    ciphered_msg = ''
    for i in range (len(key)):
        ciphered_msg += str(int(binary_msg[i]) ^ int(key[i]))
    return ciphered_msg

def decryption(encrpyted_msg, key):
    decrypted_msg = ''
    for i in range (len(key)):
        decrypted_msg += str(int(encrpyted_msg[i]) ^ int(key[i]))
    return decrypted_msg



msg = input("enter the message: ")
print("message:\n", msg)
print("\nunicode version of message:\n", str_to_unicode(msg))
binary_msg = unicode_to_binary(str_to_unicode(msg))
print("\nbinary version:\n", binary_msg)
length = len(str(binary_msg))
key = key_generator(length)
print("\nkey:\n", key)
encrypted_msg = encryption(binary_msg, key)
print("\nencrpyted message:\n", encrypted_msg)
decrypted_msg = decryption(encrypted_msg, key)
print("\ndecrpyted message:\n", decrypted_msg)
if decrypted_msg == binary_msg:
    print("successfully executed, decrypted message is the same as in the beginning")
else:
    print("unfortunately, decrypted message is not as same as given message!")
