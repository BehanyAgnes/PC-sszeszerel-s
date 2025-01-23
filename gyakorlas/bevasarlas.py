uzlet_neve = input("Adj meg az üzlet nevét: ")

bevasarlo_lista = []
while len(bevasarlo_lista) < 4:
    termek_ara = int(input(f"Adja meg a termék árát: "))
    bevasarlo_lista.append(termek_ara)

    akar_e = input("Szeretne még egy termék árát megadni? (igen/nem): ")

    if akar_e == "nem":
        break

# print(bevasarlo_lista)


print(f"Az üzlet neve: {uzlet_neve}")
print(f"Atlagos költség: {round(sum(bevasarlo_lista))/len(bevasarlo_lista)} Ft")




