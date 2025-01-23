import random
etelek =  []

while len(etelek) < 6: 
    etel = input(f"Kérem adja meg a vacsorafogás nevét:({len(etelek)+1}) ")
    etelek.append(etel)
    print(f"{len(etelek)}. {etel} hozzáadva a listához.")

print("A megadott fogások:")
index= 1
for etel in etelek: 
    print(f"{index}. étel: {etel} ")
    index += 1 

mai_ajanlat = random.choice(etelek)
print(f"A mai vacsora ajánlata: {mai_ajanlat}")

