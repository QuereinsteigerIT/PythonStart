import random


while True:
    richtige_zahl = random.randint(1,10)
    versuch = int(input("Rate eine Zahl zwischen 1 und 10: "))

    if versuch == richtige_zahl:
        print("Super, du hast richtig geraten!")
    elif versuch < richtige_zahl:
        print("Zu niedrig")
    else:
        print("Zu hoch")
    
    print("Die Zahl lautet:" , richtige_zahl)