notes = []

while True:
    note = float(input("Entrer une note (négatif pour arrêter) : "))

    if note < 0:
        break

    notes.append(note)

    print("Nombre de notes :", len(notes))
    print("Note max :", max(notes))
    print("Note min :", min(notes))
    print("Moyenne :", sum(notes) / len(notes))
    print("--------------------")