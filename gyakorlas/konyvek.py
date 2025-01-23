class Konyvek:
    def __init__(self):
        self.lista = []

    
    def beolvas(self):
        with open("konyvek.txt", "r", encoding="UTF-8") as file: 
            elso_sor = file.readline()

            sorok = file.readlines()

            for sor in sorok: 

                sor = sor.strip()
                sor = sor.split(";")

                cim = sor[0]
                ar = int(sor[1])
                eladott_peldanyok = int(sor[2])
                megjelenes_eve = int(sor[3])

                self.lista.append([cim, ar, eladott_peldanyok, megjelenes_eve])
            
            print("A könyvek listája:")

            for item in self.lista: 
                print(f"{item[0]}, {item[1]}, {item[2]}, {int(item[3])}")

        
    def kereses(self):
        pass

    
    def legolcsobb(self):
        legolcsobb = self.lista[0]

        for item in self.lista:
            if item[1] < legolcsobb[1]:
                legolcsobb = item
        
        print(f"A legocsóbb könyv: {legolcsobb[0]}, {legolcsobb[1]} Ft")
    
    def kiiratas(self):
        harry_potter = []

        for item in self.lista: 
            if "Harry Potter" in item[0]:
                harry_potter.append(item[0])
        print(harry_potter)

        with open("HarryPotter_konyvek.txt", "w", encoding="UTF-8") as file:
            file.write(f"Harry Potter könvyek kiírva a fájlba: {harry_potter}")

        
konyvek = Konyvek()
konyvek.beolvas()
konyvek.kereses()
konyvek.legolcsobb()
konyvek.kiiratas()
            
