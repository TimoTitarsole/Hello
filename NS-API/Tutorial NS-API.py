import requests
import xmltodict

auth_details = ('peter.schenkels@student.hu.nl', 'opiHlhav9xP3s-YQEj1FBFOLU7feW1278XEAVV3l7L-vsZcou_L-7w')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + input('Voer hier uw station in')
response = requests.get(api_url, auth=auth_details)

vertrekXML = xmltodict.parse(response.text)
print('Dit zijn de vertrekkende treinen:')

for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    treinsoort = vertrek['TreinSoort']

    vertrekspoor = str(vertrek['VertrekSpoor'])
    vertrekspoor = vertrekspoor[49:51]
    vertrekspoor = vertrekspoor.replace("'", '')

    vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16]          # 18:36

    print('Om '+vertrektijd+' vertrekt een '+treinsoort+' van spoor '+vertrekspoor+' naar '+ eindbestemming)