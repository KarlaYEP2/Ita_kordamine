class Album:

    def __init__(self, pealkiri, aasta, laulja):
        self.pealkiri = pealkiri
        self.aasta = aasta
        self.laulja = laulja
        self.laulud = []
    def lauljajanimi(self):
        print(self.laulja + " " + self.pealkiri + " " +  self.aasta)
    def lisa_laul(self, laul):
        self.laulud.append(laul)

    def toolaulud(self):
        for laul in self.laulud:
            print(laul.pealkiri)
