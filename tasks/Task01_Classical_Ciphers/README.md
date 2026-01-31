# Task – Classical Substitution Ciphers (Caesar & Affine)

## Description
This task implements two **classical substitution ciphers** using Python:

- **Caesar Cipher**
- **Affine Cipher**

Both algorithms operate on uppercase English letters and use **modular arithmetic** to encrypt and decrypt messages.  
These ciphers are implemented strictly for **educational purposes**, demonstrating the fundamentals of classical cryptography and key-based substitution.

The implementations are located in the same directory:
- [`caesar.py`](./caesar.py)
- [`affine.py`](./affine.py)

---

## Features
1. Encrypt and decrypt messages using classical ciphers.
2. Preserve non-alphabet characters (spaces, punctuation).
3. Automatically convert input to uppercase.
4. Use randomly generated valid keys.
5. Verify successful decryption by comparing results.

---

## Part 1 – Caesar Cipher

📄 **Implementation:** [`caesar.py`](./caesar.py)

### Description
The **Caesar Cipher** is one of the simplest encryption techniques.  
Each letter in the plaintext is shifted forward in the alphabet by a fixed number of positions called the **key**.

---

### How It Works

1. **Alphabet Mapping**  
   Each letter is mapped to an index from `0` to `25`.

2. **Encryption**  
   Each character is shifted forward by the key value:
C = (P + key) mod 26

vbnet
Copy code

3. **Decryption**  
The encrypted text is shifted backward using the same key:
P = (C - key) mod 26

yaml
Copy code

4. **Non-Alphabet Characters**  
Characters not in `A–Z` are copied unchanged.

---

### Key Details
- Alphabet: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- Key range: `0–26`
- Message input is taken from the user
- Message is converted to uppercase before processing

---

### Example Output
message: HELLO WORLD
key: 3
encrypted message: KHOOR ZRUOG
decrypted message: HELLO WORLD
successfully decrypted!

yaml
Copy code

---

### Limitations
- Only 26 possible keys (easy to brute-force)
- No lowercase support
- Not secure for real-world use

---

## Part 2 – Affine Cipher

📄 **Implementation:** [`affine.py`](./affine.py)

### Description
The **Affine Cipher** is a more advanced substitution cipher that applies both **multiplication and addition** to each character.

It uses two keys:
- `a` → multiplicative key
- `b` → additive key

---

### How It Works

1. **Alphabet Mapping**  
   Letters are mapped to values `0–25`.

2. **Encryption**
C = (aP + b) mod 26

markdown
Copy code

3. **Modular Inverse**
To decrypt, the modular inverse of `a` (mod 26) is calculated:
a × a⁻¹ ≡ 1 (mod 26)

markdown
Copy code

4. **Decryption**
P = a⁻¹(C − b) mod 26

yaml
Copy code

5. **Non-Alphabet Characters**
Characters outside `A–Z` are preserved.

---

### Key Constraints
- `a` must be **coprime with 26**
- Valid values of `a`:
[3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

yaml
Copy code
- `b` is randomly selected from `0–25`

---

### Example Output
message: HELLO
keys: a = 5; b = 8
encrypted message: RCLLA
decrypted message: HELLO
successfully decrypted!

yaml
Copy code

---
