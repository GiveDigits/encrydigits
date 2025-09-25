class DigitCipher:
    """
    A simple digit-based Caesar cipher.
    Shifts each digit in the input by a fixed amount (modulo 10).
    Non-digit characters are left unchanged.
    """

    def __init__(self, shift=3):
        self.shift = shift % 10

    def encrypt(self, text: str) -> str:
        result = []
        for char in text:
            if char.isdigit():
                shifted = (int(char) + self.shift) % 10
                result.append(str(shifted))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, text: str) -> str:
        result = []
        for char in text:
            if char.isdigit():
                shifted = (int(char) - self.shift) % 10
                result.append(str(shifted))
            else:
                result.append(char)
        return ''.join(result)

if __name__ == "__main__":
    cipher = DigitCipher(shift=3)
    secret = cipher.encrypt("1234567890")
    print("Encrypted:", secret)
    print("Decrypted:", cipher.decrypt(secret))
