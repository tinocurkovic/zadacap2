
def pozdrav(ime):
    return f"Pozdrav {ime}!"

dobrodosao = lambda ime: f"Dobrodošao {ime}!"


def pozovi_funkciju(func, ime):
    return func(ime)


rezultat = pozovi_funkciju(pozdrav, "Karlo ")
print(rezultat)


rezultat = pozovi_funkciju(dobrodosao, "Karlo")
print(rezultat)
