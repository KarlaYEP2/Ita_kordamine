from album import Album
from laul import Laul
from laulja import Laulja


lauljate_nim = []
Albumeid = []
kontroll = []
fail = open("albumid", encoding="UTF-8")
for i in fail:
    info = i.strip().split("\t")
    if info[1] not in kontroll:
        temp = Album(info[1], info[2], info[0])
        Albumeid.append(temp)
        kontroll.append(info[1])

    lauljate_nim.append(Laul(info[3],info[0], info[1])) #pealkiri,laulja, album
fail.close()
for i in Albumeid:
    for j in lauljate_nim:
        if j.album and j.laulja  == i.pealkiri and i.laulja:
            i.lisa_laul(j)


print("s")
#ALBUM -> LAULUD[]
#laul klass albumi
#laul == album
