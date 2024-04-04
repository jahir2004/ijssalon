from algemene_functies import mijn_functie_2

def inkomsten_totaal(inkomsten, btw=0.09):
    """
    Berekent het totaal van de inkomsten voor de week en het bijbehorende btw-bedrag.

    Args:
        inkomsten (list): Lijst met inkomstenwaarden voor elke dag van de week.
        btw (float, optioneel): Btw-tarief (standaard is 0.09 voor 9% btw).

    Returns:
        str: Een string met informatie over het totaal van de inkomsten en de btw.
    """
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."

def gemiddelde(mijn_lijst):
    """
    Bereken het gemiddelde van de waarden in de lijst.

    Args:
        mijn_lijst (list): Lijst met inkomstenwaarden voor elke dag van de week.

    Returns:
        str: Een string met het gemiddelde van de inkomsten.
    """
    gemiddelde_inkomsten = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten:.2f} euro."

def meervoudig(invoer_lijst):
    """
    Geeft een lijst terug van de hoogste en laagste waarde in de invoerlijst.

    Args:
        invoer_lijst (list): Lijst van integers.

    Returns:
        list: Lijst met de hoogste en laagste waarde.
    """
    hoogste, laagste = hoog_en_laag(invoer_lijst)
    return [hoogste, laagste]

# Voorbeeldgebruik
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
resultaat_inkomsten = inkomsten_totaal(inkomsten_per_dag, btw=btw_percentage)
resultaat_gemiddelde = gemiddelde(inkomsten_per_dag)
print(resultaat_inkomsten)
print(resultaat_gemiddelde)