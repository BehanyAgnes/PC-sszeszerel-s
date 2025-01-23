arak = []
uzlet_neve = input("Adja meg az üzlet nevét: ")

while len(arak) < 5: 
    
    termek_ara = int(input("Adja meg a termék árát:"))
    arak.append(termek_ara)

    valasz = input("Szeretne még egy termék árát megadni? (igen/nem): ")

    if valasz == "nem":
        break

print(arak)
print(f"Az Üzlet neve: {uzlet_neve}")
print(f"Az átlagos költség: {round((sum(arak)/len(arak)),2)} Ft")





    
    


