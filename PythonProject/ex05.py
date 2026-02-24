def max_sum(L):
    return max(L, key=sum)

def max_len(L):
    return max(L, key=len)

def max_first(L):
    return max(L, key=lambda x: x[0])

def max_last(L):
    return max(L, key=lambda x: x[-1])


L = [[1,2,3,0,-1], [13,0], [10,11,12], [0,13]]

print("max_sum :", max_sum(L))
print("max_len :", max_len(L))
print("max_first :", max_first(L))
print("max_last :", max_last(L))