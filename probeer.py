mijn_dictionary = {
    "voornaam" : "harry",
    "achternaam" : "van winkel",
     "geboortedatum" : "27-3-1939", 
}
print()
for k, v in mijn_dictionary.items():
 print(k, v)
 print(f"voornaam: {mijn_dictionary['voornaam']} ")
 mijn_dictionary["voornaam"] = "hendrikus"
 print()
for k, v in mijn_dictionary.items():
 print(k, v)
