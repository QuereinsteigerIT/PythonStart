
# Stream 3 21.04.24

#Strings zusammensetzen
# verbinden = "Hallo " + "Welt"
# print(verbinden)


#Einen String mit upper und lower komplett groß oder klein schreiben
# begruessung = "GooGlE.com"
# print(begruessung.lower())
# print(begruessung.upper())


# Wir haben einen Satz mit split() an den Lehrzeichen getrennt und in einer For-Schleife ausgegeben
# satz = "Cool, dass Ihr alle da seid!"
# woerter = satz.split()
# print(woerter)

# for wort in woerter:
#     print(wort)


# Ausgabe alles Elemente auf einer Liste mit einer For-Schleife
# zahlen = [1,2,3,4,5,7]
# # print(zahlen)

# for zahl in zahlen:
#     print(zahl)


# Wir schreiben eine eigene Fruntion

# def multi(x,y):
#     return x * y

# print(multi(3,5))


# Wir überschreiben mit einer Funktion eine Globale Variable
# meineVariable = 15
# print(meineVariable)

# def alleskoenner(x):
#     global meineVariable
#     meineVariable = x
#     return meineVariable 

# alleskoenner(16)

# print(meineVariable)

# meineVariable = 15
# print(meineVariable)
# alleskoenner(17)

# print(meineVariable)

#Wenn Bedingungen

# alter = 16

# if alter >= 18:
#     print("Du bist volljährig.")
# elif alter < 18 and alter >= 16:
#     print("Du bist nicht volljährig aber darfst bis 22 Uhr rein.") 
# else:
#     print("Du bist nicht volljährig.")



# Unser Wecker Zeigt die Tageszeit an mit Bedingungen der Zeit
# uhrzeit = 21

# if uhrzeit > 6 and uhrzeit < 12:
#     print("Es ist Vormittag.")
# elif uhrzeit > 12 and uhrzeit < 17:
#     print("Es ist Nachmittags.")
# elif uhrzeit > 17 and uhrzeit < 20:
#     print("Es ist Abend.")
# else:
#     print("Es ist Nacht.")


count = 1

while count <= 5:

    print(count)
    count += 1