# variante du script
# variante du script
print("Bienvenu dans la calculatrice v1 : On additionne. Merci de suivre les instructions demandées")
finput = ""

while (finput.isdigit() == False):
    finput = input("Merci de renseigner le 1er nombre : ")
nombre1 = int(finput)

finput = ""
while (finput.isdigit() == False):
    finput = input("Merci de renseigner le 2nd nombre : ")
nombre2 = int(finput)

resultat = nombre1 + nombre2

print(
    f"Le résultat de l'addition du nombre {nombre1} avec le nombre {nombre2} est égal à {resultat}")
