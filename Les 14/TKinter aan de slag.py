from tkinter import *
import requests
import xmltodict


def clicked():
    invoerstation = entry.get()
    auth_details = ('peter.schenkels@student.hu.nl', 'opiHlhav9xP3s-YQEj1FBFOLU7feW1278XEAVV3l7L-vsZcou_L-7w')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + invoerstation
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)

    aantal = 0
    ding1 = ''
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        aantal += 1
        if aantal < 6:
            eindbestemming = vertrek['EindBestemming']

            treinsoort = vertrek['TreinSoort']

            vertrekspoor = str(vertrek['VertrekSpoor'])
            vertrekspoor = vertrekspoor[49:51]
            vertrekspoor = vertrekspoor.replace("'", '')

            vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
            vertrektijd = vertrektijd[11:16]  # 18:36
            ding1 += 'Om ' + vertrektijd + ' vertrekt een ' + treinsoort + ' van spoor ' + vertrekspoor + ' naar ' + eindbestemming + '\n'
        else:
            break
    label["text"] = ding1


root = Tk()

root.configure(background='yellow')

label = Label(master=root,text='Voer hier uw station in.', background='yellow', foreground='blue', font=('Helvetica', 11, 'bold'), height=2)
label.pack()

entry = Entry(master=root, font=('Helvetica', 11))
entry.pack(padx=180, pady=0)

button = Button(master=root, text='Zie stations', font=('Helvetica', 11), command=clicked)
button.pack(pady=10)

label = Label(master=root,text='Vertrektijden:',background='yellow', foreground='blue', font=('Helvetica', 11, 'bold'), height=2)
label.pack()

label = Label(master=root,text='',background='yellow', foreground='blue', font=('Helvetica', 10), height=6)
label.pack(padx=10, pady=10)

root.mainloop()