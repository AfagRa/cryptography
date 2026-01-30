# Task – One-Time Pad (OTP) Encryption

## Description
This task implements a **One-Time Pad (OTP)** encryption scheme using Python.  
The program converts a plaintext message into its **binary representation**, generates a random key of the same length, and performs **XOR encryption** to produce a ciphered message. It also supports decryption back to the original message.

OTP is a classical cryptographic method that is theoretically **unbreakable** if the key is truly random, used only once, and kept secret.

---

## Features
1. Convert a string message to **Unicode numbers**.
2. Convert Unicode numbers to **binary representation**.
3. Generate a **random binary key** equal in length to the binary message.
4. Encrypt the message using **bitwise XOR** with the key.
5. Decrypt the message using the same key.
6. Verify that the decrypted message matches the original.

---

## How It Works

1. **Message to Unicode**  
   Each character in the message is converted to its Unicode integer value.

2. **Unicode to Binary**  
   Unicode values are converted into 8-bit binary strings, then concatenated to form the full binary message.

3. **Key Generation**  
   A random binary key is generated with the same length as the binary message.

4. **Encryption & Decryption**  
   Each bit of the binary message is XORed with the corresponding bit of the key:
   ```text
   0 XOR 0 = 0
   0 XOR 1 = 1
   1 XOR 0 = 1
   1 XOR 1 = 0
