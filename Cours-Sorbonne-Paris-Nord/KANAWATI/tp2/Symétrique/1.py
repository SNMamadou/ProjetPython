def cesar_chiffre(t, decalage=3):
    resultat = ""
    for caractere in t:
        if caractere.isalpha():
            # détermine le code de base (majuscule ou minuscule)
            base = ord('A') if caractere.isupper() else ord('a')
            # applique le décalage modulo 26
            resultat += chr((ord(caractere) - base + decalage) % 26 + base)
        else:
            # les caractères non alphabétiques ne sont pas modifiés
            resultat += caractere
    return resultat

# Exemple d'utilisation
message = "Bonjour le Monde !"
chiffre = cesar_chiffre(message)
print("Message chiffré :", chiffre)


