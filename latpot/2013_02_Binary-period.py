"""
Note: many errors, need to fix
"""
def binary_period(N):
    bistring = bin(N)[2:]
    index = 0
    half = int((len(bistring)-1)/2)
    for i in range(half):
        if bistring[i] == bistring[i+half]:
            index += 1
        else:
            break

    if index == 0:
        return -1
    else:
        return index

##==================================
print(str(binary_period(955)))
