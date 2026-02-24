def trier(classeur, valeur):
    if valeur < 0:
        classeur['négatifs'].append(valeur)
    else:
        classeur['positifs'].append(valeur)
    return classeur


classeur = {'négatifs': [], 'positifs': []}

print(trier(classeur, -5))
print(trier(classeur, 8))