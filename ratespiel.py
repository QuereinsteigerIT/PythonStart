import random


while True:
    richtige_zahl = random.randint(1,10)

    try:
        versuch = int(input("Rate eine Zahl zwischen 1 und 10:  Mit 0 kannst du das Spiel beenden!"))
    except ValueError:
        print("Gibt bitte eine gültige Zahl ein!")
        continue

    if versuch == 0:
        print("Das Spiel wurde beendet")
        break
    elif versuch == richtige_zahl:
        print("Super, du hast richtig geraten!")
    elif versuch < richtige_zahl:
        print("Zu niedrig")
    else:
        print("Zu hoch")
    
    print("Die Zahl lautet:" , richtige_zahl)