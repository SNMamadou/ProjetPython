![[Initiation_Programmation_Le langage Python.pdf]]

##### Le langage (les entrées/sorties)

1. print('Je suis nouveau en python !')
![[Pasted image 20250916105313.png]]

2. Print("Mamadou")
![[Pasted image 20250916105454.png]]

3. Mon nom est pris pour une variable
![[Pasted image 20250916105836.png]]

4. Il comprend qu'il y a une erreur et qu'il manque des parenthèses
![[Pasted image 20250916110119.png]]

5. Plusieurs print sur la meme ligne ne sont pas autorisé
![[Pasted image 20250916110342.png]]

6. Nouveau est ajouté juste après "suis"
![[Pasted image 20250916110739.png]]

Recherchez l'utilisation de l'argument sep dans la fonction print().

```
valeur1 = 'test1'
valeur2 = 'test2'
print(valeur1, valeur2, ..., sep="séparateur")
```

![[Pasted image 20250916113123.png]]

Il est possible de préciser sur combien de caractères le résultat doit être écrit et comment se fait l'alignement (à gauche (<), à droite (>) ou centré (^)).

```
print(f"{10:>10d}"); print(f"{1000:>10d}")
```

![[Pasted image 20250916114825.png]]

La fonction input() : est capable de lire les données saisies par l’utilisateur et de renvoyer les mêmes données au programme en cours d’exécution.

```
mon_nom = input("Saisir votre nom complet : ")
print(type(mon_nom))
```
![[Pasted image 20250916115118.png]]

La fonction input() lit les données saisies par l’utilisateur et les envoie au programme en cours d’exécution.

```
maVariable = input("Saisissez un chiffre : ")
monResultat = maVariable ** 2
print(maVariable, "au carré est :", monResultat)
```
![[Pasted image 20250916115652.png]]

Ecrire un programme en Python qui demande l’âge d’un enfant à l’utilisateur. Ensuite, il l’informe de sa catégorie : 

- « Poussin » de 6 à 7 ans 
- « Pupille » de 8 à 9 ans 
- « Minime » de 10 à 11 ans 
- « Cadet » après 12 ans 

```
print("Ecrire 0 pour la fin")

  

while True:

age = int(input("Quel est l'age de l'enfant ? : "))

  

if age == 7 or age == 6 :

print("L'enfant est un poussin car il a : ", age)

elif age == 8 or age == 9 :

print("L'enfant est une pupille car il a : ", age)

elif age == 10 or age == 11 :

print ("L'enfant est minime car il a : ", age)

elif age > 11 :

print("Trop vieux, ", age)

elif age == 0 :

print("Fin des questions")

break
```


Ecrire un programme en Python qui permette 
1. Entrer deux nombres. 
2. Choisir une opération (+, -, , /). 
3. Selon l'opération choisie, effectuer le calcul correspondant. 
4. Gérer le cas spécial de la division par zéro. 5. Afficher le résultat. 

```
print("Pour quitter la boucle écrire 'end'")

  

while True:

A = int(input(("Entrer le premier nombre : ")))

B = int(input(("Entrer le 2e nombre : ")))

R = 0

  

choix = input("Choisir une opération entre : +, -, * et / :")

  

if choix == "+":

R = A + B

print(f"Le résultat est : ",R)

elif choix == "-":

R = A - B

print(f"Le résultat est : ",R)

elif choix == "*" :

R = A * B

print(f"Le résultat est : ",R)

elif choix == "/" :

R = A / B

print(f"Le résultat est : ",R)

elif choix == "end":

break

else:

print("Il faut bien répondre a la question")
```

