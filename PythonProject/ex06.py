def tuple_to_dict(L):
    return {i: L[i] for i in range(len(L))}


L = [(1,2), (3,6), (9,0)]

print(tuple_to_dict(L))