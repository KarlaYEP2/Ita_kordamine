class Laulja:

    def __init__(self, nimi):
        self.nimi = nimi
        self.albumid = []
        self.laulud = []
    def lisa_album(self, album):
        self.albumid.append(album)
        for i in album.albumid:
            self.laulud.append(i)
    def nimetused(self):
        print(self.nimi)

    def albumiid(self):
        for album in self.albumid:
            album.nimetused()

