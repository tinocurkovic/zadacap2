import random
imena_studenta = ["Gingis Kan", "Pol Pot", "Stalin", "Adolf", "Esmeralda"]
ocjene = {}
for ime in imena_studenta:
    ocjena = random.randint(1, 5)  
    ocjene[ime] = ocjena  
    if ocjena in ocjene:
        ocjene[ocjena] += 1
    else:
        ocjene[ocjena] = 1
for ime, ocjena in ocjene.items():
    print(f"{ime}: {ocjena}")
prolazni = sum(ocjene[ocjena] for ocjena in ocjene if ocjena > 1)
ukupno = sum(ocjene.values())
postotak_prolaznosti = (prolazni / ukupno) * 100

print(f"Postotak prolaznosti: {postotak_prolaznosti:.2f}%")
