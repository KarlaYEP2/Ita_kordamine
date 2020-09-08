from album import Album
from laul import Laul
from laulja import Laulja

albumid = []
artist = []
album = []
test = []
fail = open("albumid", encoding="UTF-8")
for i in fail:
    info = i.strip().split("\t")
    print(info)
    if not info[0] in artist:
        artist.append(info[0])
    if not info[1] in album:
        album.append(info[1])
    albumid.append(Album(info[1], info[2], info[0])) #pealkiri, aasta, laulja
print(artist)
print(albumid)
fail.close()
#ALBUM -> LAULUD[]
#
