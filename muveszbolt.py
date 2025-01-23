lista = []

with open("termekek.txt", "r", encoding="UTF-8") as file:
    elsosor = file.readline()       # ha van a forrásfájlban első fölösleges sor
    for sor in file:
        adat = sor.strip().split(";")
        lista.append([adat[0], int(adat[1]),int(adat[2]), int(adat[3])])

print("A fájl tartalma:")
for i in lista:
    print(f"{i[0]};{i[1]};{i[2]};{i[3]}")

draga = lista[0]
for i in lista:
    if draga[1] < i[1]:
        draga = i
print(f"\nA legdrágább termék: {draga[0]} ({draga[1]} Ft)")

ossz = 0
for i in lista:
    ossz += i[2]
print(f"Az eladott termékek darabszámának átlaga: {round(ossz / len(lista), 1)} Ft")

C_sek = []
for i in lista:
    if i[0][0] == "C":      # VAGY if i[0].startswith("C"):
        C_sek.append(i)

print(f"A C-vel kezdődő termékek száma: {len(C_sek)}")

with open("C_betus_termekek.txt", "w", encoding="UTF-8") as fajl:
    for i in C_sek:
        print(f"{i[0]};{i[1]};{i[2]};{i[3]}")
        fajl.write(f"{i[0]};{i[1]};{i[2]};{i[3]}\n")
