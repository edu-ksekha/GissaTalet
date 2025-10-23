namn = input("Vad heter du?:")
print(f"Hej {namn} och välkommen till spelet!")

import random as rand
hemligt_tal= rand.randint(1,10)
gissning = input("Gissa ett tal mellan 1 och 10:")
print(f"Tyvärr, det var {hemligt_tal}")
