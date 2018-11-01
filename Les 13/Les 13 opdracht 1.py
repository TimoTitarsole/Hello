import xmltodict

with open("producten.xml", "r") as f:
    xmldict = xmltodict.parse(f.read())

    for artikel in xmldict["artikelen"]["artikel"]:
        print(artikel["naam"])