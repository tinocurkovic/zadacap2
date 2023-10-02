import random

radnici = [
    "John Wayne", "Will Smith", "Mark Johnson", "Emily Davis", "Michael Wilson",
    "Sarah Anderson", "David Taylor", "Olivia Brown", "James Miller", "Emma Garcia",
    "Daniel Martinez", "Sophia Thomas", "Robert Jackson", "Isabella White", "Joseph Lee"
]

radnici_lista = []


for radnik in radnici:
    ime, prezime = radnik.split()
    satnica = round(random.uniform(4, 6), 2)
    tjedni_sati = random.randint(20, 30)
    radnik_dict = {
        "ime": ime,
        "prezime": prezime,
        "satnica": satnica,
        "tjedni_sati": tjedni_sati
    }
    radnici_lista.append(radnik_dict)

isplate = []


for radnik in radnici_lista:
    ime = radnik["ime"]
    prezime = radnik["prezime"]
    satnica = radnik["satnica"]
    tjedni_sati = radnik["tjedni_sati"]
    isplata = round(satnica * tjedni_sati, 2)
    isplate.append((ime, prezime, isplata))

ukupna_isplata = sum(isplata for _, _, isplata in isplate)
prosjecna_isplata = ukupna_isplata / len(radnici_lista)

print("Podaci o isplatama:")
for ime, prezime, isplata in isplate:
    print(f"{ime} {prezime}: {isplata}")

print(f"\nUkupna isplata za tjedan: {ukupna_isplata}")
print(f"Prosječna isplata za tjedan: {prosjecna_isplata}")

print("\nRadnici s isplatom iznad prosjeka:")
for ime, prezime, isplata in isplate:
    if isplata > prosjecna_isplata:
        print(f"{ime} {prezime}")
