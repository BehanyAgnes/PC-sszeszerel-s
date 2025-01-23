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

        print(self.lista)

        print("A könvyek listája:")

        for item in self.lista: 
           print(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}")

    def legregibb(self):

        print("--------------------------------------")

        for item in self.lista: 

            if item[3] > 2010:

                print(f"A 2010 után megjelent könvyek: \n {item[0]}; {item[1]}; {item[2]}; {item[3]}")

            
    def legolcsobb(self):

        print("--------------------------------------")

        legolcsobb = self.lista[0]

        for item in self.lista: 
            if item[1] < legolcsobb[1]:
                legolcsobb = item
            
        print(f"A legolcsóbb könyv: {legolcsobb[0]} {legolcsobb[1]} Ft")
    
   

    def Harry(self):

        print("--------------------------------------")

        Harry_Potter = []

        for item in self.lista: 

            if item[0].startswith("Harry"):

                Harry_Potter.append(item[0])
        
        print("A Harry Potter könvyek kiírása fájlba:")

        print(f"{Harry_Potter[0]}, \n {Harry_Potter[1]},  \n {Harry_Potter[2]}")

   

        with open("HarryPotter_konyvek.txt", "w", encoding="UTF-8") as file:
            file.write(f"Harry Potter könyvek kiírva a fájlba: \n {Harry_Potter[0]}, \n {Harry_Potter[1]}, \n {Harry_Potter[2]}")

konyvecske = Konyvek()
konyvecske.beolvas()
konyvecske.legregibb()
konyvecske.legolcsobb()
konyvecske.Harry()


