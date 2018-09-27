def standaardprijs(afstandKM):
    if afstandKM <= 50 and afstandKM > 0:
        defprijs = afstandKM * 0.80
        return defprijs
    if afstandKM >50:
        defprijs = afstandKM * 0.60 + 15.00
        return defprijs
    if afstandKM <= 0:
        defprijs = 0
        return defprijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == 'ja':
            eindprijs = standaardprijs(afstandKM) * 0.65
        if weekendrit == 'nee':
            eindprijs = standaardprijs(afstandKM) * 0.70
    else:
        if weekendrit == 'ja':
            eindprijs = standaardprijs(afstandKM)
        if weekendrit == 'nee':
            eindprijs = standaardprijs(afstandKM) * 0.60
    print(eindprijs)

afstandKM = (float(input('Hoevoel KM is je reis?')))
leeftijd = (float(input('Wat is uw leeftijd?')))
weekendrit = (input('Is je reis in het weekend?'))

ritprijs(leeftijd, weekendrit, afstandKM)