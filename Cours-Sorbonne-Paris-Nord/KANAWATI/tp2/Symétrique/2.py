def vigenere_chiffre(t, cle):
    resultat = ""
    cle = cle.lower()
    index_cle = 0

    for caractere in t:
        if caractere.isalpha():
            # Décalage basé sur la lettre de la clé (0 à 25)
            decalage = ord(cle[index_cle % len(cle)]) - ord('a')
            base = ord('A') if caractere.isupper() else ord('a')
            chiffre = chr((ord(caractere) - base + decalage) % 26 + base)
            resultat += chiffre
            index_cle += 1
        else:
            # Les caractères non alphabétiques ne sont pas modifiés
            resultat += caractere

    return resultat

# Exemple d'utilisation
message = "Bonjour le Monde !"
cle = "SECURITE"
chiffre = vigenere_chiffre(message, cle)
print("Message chiffré :", chiffre)

