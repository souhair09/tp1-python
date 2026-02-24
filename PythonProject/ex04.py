def selection(L1, L2):
    resultat = []

    for i in L2:
        if -len(L1) <= i < len(L1):
            resultat.append(L1[i])
        else:
            resultat.append(None)

    return resultat


L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L2 = [0, 2, -1, 9, 100]

print(selection(L1, L2))