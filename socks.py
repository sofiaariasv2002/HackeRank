def sockMerchant(ar):
    ar.sort()
    cant=0
    tam=len(ar)
    while tam > 0:
        par=ar.count(ar[0]) #obtener cuantas veces se repite el numero
        cant=cant+(par//2) #obtener la cantidad de pares 
        i=ar[0] 
        ar[:] = [x for x in ar if x != i] #quitar el indice que ya se sumo
        tam=len(ar)
        
    return cant

if __name__ == '__main__':
    ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]
    print (sockMerchant(ar))