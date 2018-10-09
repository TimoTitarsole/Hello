def gemiddelde(zin):
    lengte = len(zin.replace(' ', ''))
    woorden = len(zin.split())
    print(lengte / woorden)


gemiddelde(input('Voer een willekeurige zin in:'))