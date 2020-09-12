from album import Album
from laul import Laul
from laulja import Laulja

#TAGAPOOLSE OSA ALGUS
lauljate_nim = []
Albumeid = []
kontroll = []
Lauljad = []
fail = open("albumid", encoding="UTF-8")
for i in fail: #VÕTAB FAILIST ASJAD VÄLJA JA PANEB INFOSSE
    info = i.strip().split("\t")
    if info[1] not in kontroll: #JAGAB ASJAD INFOST UUDE LOETELLU
        temp = Album(info[1], info[2], info[0])
        Albumeid.append(temp)
        kontroll.append(info[1])

    lauljate_nim.append(Laul(info[3], info[0], info[1])) #pealkiri,laulja, album LOETELU
    Lauljad.append(Laulja(info[0]))#nimi LOETELU


for i in Albumeid: #VAATAB, KUI KAKS ALMBUIT ON SAMAD LÜKKAVAD NAD LISA ASJU LOETELLUTE SISSE
    for j in Lauljad:
        if i.laulja == j.nimi:
            j.laulud.append(i)
            j.albumid.append(i)


for i in Albumeid: #21
    for j in lauljate_nim:
        if j.album == i.pealkiri:
            i.laulud.append(j)
fail.close()
#MENÜÜ ALGUS
#KÜSIB MILLE JOAKS VAJA
print("Vali:")
print("1: Väljasta terve sisu")
print("2: Väljasta albumid pealkirja järgi, või aasta numbri järgi")
print("3: Otsi failist laulu nime järgi")
print("4: Otsida failist laulja")
Valik = input(str("Valik: "))
#KUI VALIB 1 SIIS TOOB VÄLJA VAJALIKU INFORMATSIOONI
if Valik == "1":
    for temp in Albumeid:
        temp.lauljajanimi()
        temp.toolaulud()
        print("----------------")
#KUI VALIB 2 LEIAB LOETELUST INFO VASTAVALT VALIKULE
elif Valik == "2":
    otsing = input("aasta või album: ")
    for temp in Albumeid:
        if otsing in temp.pealkiri or otsing == temp.aasta: # KUI OTSITAV ON VÕRDNE ALBUMI JA AASTAGA TOOB VÄLJA VAJALIKU INFO
            temp.toolaulud()
            temp.lauljajanimi()
#KUI VALIKUSSE LÄHEB 3...
elif Valik == "3":
    otsing = input("Leia nime järgi: ")
    for temp in Albumeid:
        for lauljate_nim in temp.laulud:
            if otsing.lower() in lauljate_nim.pealkiri.lower(): #MINGI STRINGI ERRORI TÕTTU LÜKKASIN LISAKS LOWERID
                temp.lauljajanimi()
                lauljate_nim.toopealkirjad()
#VALIK 4
elif Valik == "4":
    otsing = input("Leia laulja järgi: ")
    for laulja in Lauljad:
        if otsing.lower() in laulja.nimi.lower():
            for temp in laulja.albumid:
                temp.lauljajanimi()


