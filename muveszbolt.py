class Termekek:
    def __init__(self, nev, ar, db, ev):
        self.nev = nev
        self.ar = int(ar)
        self.db = int(db)
        self.ev = int(ev)

    def __str__(self):
        return f"{self.nev};{self.ar};{self.db};{self.ev}"
    
def beolvasas(txt):
    tomb = []
    with open(txt, "r", encoding="UTF-8") as file:
        elsosor = file.readline()       # ha van első felesleges sor
        for sor in file:
            adat = sor.strip().split(";")
            tomb.append(Termekek(adat[0], adat[1], adat[2], adat[3]))
    return tomb

lista = beolvasas("termekek.txt")
# ha kérne valami ilyesmit:
# print("A fájl tartalma " + "\n".join(map(str,lista)))

print("A fájl tartalma:")
for i in lista:
    print(i)

# az összes feladat egy ciklusban:
draga = lista[0]
ossz = 0
C_sek = []
for i in lista:
    ossz += i.db

    if draga.ar < i.ar:
        draga = i
    
    if i.nev[0] == "C":
        C_sek.append(i)

print(f"\nA legdrágább termék: {draga.nev} ({draga.ar} Ft)")
print(f"Az eladott termékek darabszámának átlaga: {round(ossz / len(lista), 1)}")
print(f'"C"-vel kezdődő termékek száma: {len(C_sek)}')

print('"C"-vel kezdődő termékek:')
with open("C_betus_termekek.txt", "w", encoding="UTF-8") as fajl:
    fajl.write("\n".join(map(str,C_sek)))
    print("\n".join(map(str,C_sek)))
