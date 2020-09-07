from album import Album
from laul import Laul
# testime laulu objekti loomist
from laulja import Laulja

laul_1 = Laul("Maanteepõrgusse", "ACDC")
#print(laul_1.laulja, laul_1.pealkiri)
laul_2 = Laul("12", "ACDC")
#print(laul_2.laulja, laul_2.pealkiri)
laul_3 = Laul("Välk", "ACDC")
#print(laul_1.laulja, laul_1.pealkiri)
laul_4 = Laul("Thunderstruck", "ACDC")
#print(laul_2.laulja, laul_2.pealkiri)
# testime albumi loomist
album_1 = Album("Uus album 1", 2019, "ACDC")
# lisame laulud albumisse
album_1.lisa_laul(laul_1)
album_1.lisa_laul(laul_2)
# testime albumi loomist
album_2 = Album("Uus album 2", 2019, "ACDC")
# lisame laulud albumisse
album_2.lisa_laul(laul_3)
album_2.lisa_laul(laul_4)
# vaatame loodud albumi sisu
#print(album_2.pealkiri)
#for laul in album_2.laulud:
#    print(laul.laulja, laul.pealkiri)
# testime Laulja loomist
laulja = Laulja("ACDC")
laulja.lisa_album(album_1)
laulja.lisa_album(album_2)
# testime albumite sisu
for album in laulja.albumid:
    print(album.pealkiri)
    for laul in album.laulud:
        print(laul.laulja, laul.pealkiri)

fail = open("albumid")
Laulja