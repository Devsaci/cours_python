print("hello")
print("C:\Git\mingw64")

###########################################
# 64. Les chaînes de caractères
site = 'docstring'

print(site[0])  # d
print(site[4])  # t


# longue_phrase  et guillemets doubles

age = "J'ai 26 ans"  # Avec guillemets doubles
age = 'J\'ai 26 ans'  # Avec guillemets simples
longue_phrase = '''Bonjour,
bienvenue sur Docstring, 
on espère que vous appréciez 
ce glossaire sur les chaînes
de caractères 🙂
'''
# 99. Changer la casse

site = 'docstring'

print(site[0:3])  # 'doc'
print(site[3:])   # 'string'
print(site[1::2])  # 'osrn'


# 99. Changer la casse
a = "ftgiutfitk"
b = a.upper()
print(b)  # FTGIUTFITK

a = "DJKFRGJKPR"
b = a.lower()
print(b)  # djkfrgjkpr

a = "sdfghjklmù*"
b = a.capitalize()
print(b)  # Sdfghjklmù*

a = "sdfghjklmù*  fghjklm fghjklm gbhnj,k; "
b = a.title()
print(b)  # Sdfghjklmù*  Fghjklm Fghjklm Gbhnj,K;


# 100. Remplacer des éléments

a = "bonjour"
b = a.replace("jour", "soir")
print(b)  # bonsoir
