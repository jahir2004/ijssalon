def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag/personen
    return f"Het bedrag per persoon is {bedrag_pp} euro"

b = int(input("Welk bedrag zit er in de fooienpot? "))
p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))


print(fooi_pp(b,p))

def som(dictionary):
    return sum(dictionary.values())


from helper import som
totaal_inkomsten = som("inkomsten")





