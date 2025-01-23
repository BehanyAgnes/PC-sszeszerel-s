import random
jatekok = []

db = 1
print("Add meg a 4 kedvenc videójátékodat!")
while True:
    kedvenc = input(f"{db}. játék: ")
    jatekok.append(kedvenc)
    db += 1

    if db > 4:
        print(f"A kedvenc videójátékaid: {jatekok[0]}, {jatekok[1]}, {jatekok[2]}, {jatekok[3]}")
        break

kedvenc_jatekok = random.choice(jatekok)

print(f"A 2025. év játéka: {kedvenc_jatekok}")


