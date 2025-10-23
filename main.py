namn = input("Vad heter du?:")
print(f"Hej {namn} och välkommen till spelet!")

import random as rand
hemligt_tal= rand.randint(1,10)
gissning = int(input("Gissa ett tal mellan 1 och 10:"))
if gissning == hemligt_tal:
    print("Du har rätt!")
else:
    print(f"Tyvärr, det var {hemligt_tal}")
print("Nu ska du köra igen, med flera försök!")

antal_gissningar = 0
while True:
    gissning_igen = int(input("Ge mig gissning mellan 1 och 10:"))
    antal_gissningar += 1
    if gissning > hemligt_tal:
        print(f"Försök {antal_gissningar}: Fel")
    elif gissning < hemligt_tal:
        print(f"Försök {antal_gissningar}: Fel")
    else:
        print(f"Försök {antal_gissningar}: Rätt gissat!")
        break
