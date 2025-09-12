d = 2753
n = 3233
e = 17

def sign_char(c, d, n):
    m_int = ord(c)  # convertit un caractère en entier (ASCII)
    signature = pow(m_int, d, n)
    return signature

def verify_char(c, signature, e, n):
    m_int = ord(c)
    m_from_sig = pow(signature, e, n)
    return m_int == m_from_sig

message = "HELLO"
signatures = [sign_char(c, d, n) for c in message]

print("Message :", message)
print("Signatures :", signatures)

valid = all(verify_char(c, sig, e, n) for c, sig in zip(message, signatures))
print("Signature valide !" if valid else "Signature invalide.")


