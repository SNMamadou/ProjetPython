# Clés RSA (faibles pour l'exemple)
e = 17
d = 2753
n = 3233

# Fonction de signature caractère par caractère
def sign_char(c, d, n):
    return pow(ord(c), d, n)

# Fonction de vérification
def sig_valide(c):
    message, signatures = c
    if len(message) != len(signatures):
        return False
    for caractere, sig in zip(message, signatures):
        if ord(caractere) != pow(sig, e, n):
            return False
    return True

# Signature du message "HI"
message = "HI"
signatures = [sign_char(c, d, n) for c in message]
document = (message, signatures)

print("Message :", message)
print("Signatures :", signatures)
print("Signature valide :", sig_valide(document))


