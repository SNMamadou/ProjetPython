def vigenere_dechiffre(t, cle):
    resultat = ""
    cle = cle.lower()
    index_cle = 0

    for caractere in t:
        if caractere.isalpha():
            decalage = ord(cle[index_cle % len(cle)]) - ord('a')
            base = ord('A') if caractere.isupper() else ord('a')
            dechiffre = chr((ord(caractere) - base - decalage) % 26 + base)
            resultat += dechiffre
            index_cle += 1
        else:
            resultat += caractere

    return resultat

# Exemple d'utilisation
message_chiffre = "Thptsmv pi Hrcvii !"  # ← Chiffré avec la clé "SECURITE"
cle = "SECURITE"

print("Message déchiffré :", vigenere_dechiffre(message_chiffre, cle))
