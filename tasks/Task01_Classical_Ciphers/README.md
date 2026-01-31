# Task – Classical Substitution Ciphers (Caesar & Affine)

## Description
This task implements two classical substitution ciphers in Python:

- **Caesar Cipher**: shifts letters by a fixed key.  
- **Affine Cipher**: uses multiplication and addition with two keys.

Both ciphers work on uppercase letters, preserve non-alphabet characters, and use modular arithmetic. These implementations are for **educational purposes**.

---

## Features

### Caesar Cipher
- Encrypts and decrypts messages using a single numeric key.
- Automatically converts input to uppercase.
- Preserves spaces and punctuation.
- Randomly generates key between 0–26.
- Example formula:

Encryption: C = (P + key) mod 26
Decryption: P = (C - key) mod 26

markdown
Copy code

### Affine Cipher
- Encrypts and decrypts using two keys: a (multiplicative) and b (additive).
- a must be coprime with 26; b can be 0–25.
- Automatically converts input to uppercase.
- Preserves spaces and punctuation.
- Example formula:

Encryption: C = (a * P + b) mod 26
Decryption: P = inverse(a) * (C - b) mod 26

yaml
Copy code
where inverse(a) is modular inverse of a modulo 26.

---

## Files
- [`caesar.py`](./caesar.py)  
- [`affine.py`](./affine.py)  

Each file contains:
- Functions for encryption and decryption.
- Random key generation (Caesar) or valid key selection (Affine).
- Verification of decryption correctness.

---

## Example Outputs

**Caesar Cipher**
Message: HELLO
Key: 3
Encrypted: KHOOR
Decrypted: HELLO


**Affine Cipher**
Message: HELLO
Keys: a = 5, b = 8
Encrypted: RCLLA
Decrypted: HELLO