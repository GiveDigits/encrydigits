# givedigits-encryption

Digit-focused encryption algorithms, utilities, and educational tools.

## What is this?

**givedigits-encryption** explores creative ways to encrypt and decrypt numbers and digit strings.  
It includes digit ciphers, number-based encoding, and tools for learning about basic cryptography.

## Features

- Simple digit shift cipher (like Caesar, but for digits).
- Easily extendable for more ciphers and utilities.
- Educational code comments.

## Usage

Encrypt and decrypt digit strings using Python:

```python
from givedigits_encryption import DigitCipher

cipher = DigitCipher(shift=3)
encrypted = cipher.encrypt("1234567890")
decrypted = cipher.decrypt(encrypted)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
```

## Next steps

- Add more ciphers (substitution, modular, etc)
- CLI and web API
- Jupyter notebooks for education
