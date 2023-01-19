# Caculatrice fonction
a = input("Entrez un nombre a :  ")
print(a)  # retourn chaine de caractere
b = input("Entrez un nombre b :  ")
print(b)
print(
    f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")

# {} affiche la variable
# int() transforme str -> int

# variante du script

a = int(input("Entrez un nombre a :  "))
print(a)  # retourn chaine de caractere
b = int(input("Entrez un nombre b :  "))
print(b)
print(
    f"Le résultat de l'addition de {a} avec {b} est égal à {a + b}")
