prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}

aanbieding = prijzen["vanille"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding:.2f}"
reclame_tekst2 = reclame_tekst[:reclame_tekst.index(".") + 3]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()

for el in reclame_tekst4:
    print(el.upper())