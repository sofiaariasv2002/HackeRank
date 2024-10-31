##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (hash Tables)
# 30 oct 2024
##################################################################################################################

##################################################################################################################
# You are given an array and you need to find number of tripets of indices (i,j,k) such that the elements at 
# those indices are in geometric progression for a given common ratio r and i<j<k .
##################################################################################################################

def countTriplets(arr, r):
    pairs = dict()     # Almacena pares potenciales para el triplete
    triplets = dict()  # Almacena tripletas completas posibles
    count = 0          # Cuenta el total de tripletas válidas

    for val in arr:
        # Si `val` completa alguna tripleta, se suma esa cantidad al conteo final.
        if val in triplets:
            count += triplets[val]
        
        # Si `val` puede ser el segundo elemento de una tripleta, prepara `val * r` como posible final de tripleta.
        if val in pairs:
            if val * r in triplets:
                triplets[val * r] += pairs[val]
            else:
                triplets[val * r] = pairs[val]
        
        # Añade `val` como un inicio potencial de un par.
        if val * r in pairs:
            pairs[val * r] += 1
        else:
            pairs[val * r] = 1
    
    return count             

if __name__ == '__main__':
    arr = [1, 2, 2, 4]
    r = 2
    print(countTriplets(arr, r))
