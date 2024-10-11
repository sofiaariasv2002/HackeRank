##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit
# 17 sep 2024
##################################################################################################################
##################################################################################################################
# It is New Year's Day and people are in line for the Wonderland rollercoaster ride. 
# Each person wears a sticker indicating their initial position in the queue from 1 to n. 
# Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. 
# One person can bribe at most two others.

# Determine the minimum number of bribes that took place to get to a given queue order. 
# Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
##################################################################################################################

def minimumBribes(q):
    cont = 0  # Contador de sobornos

    for i in range(len(q)): 
        actual = q[i]  # Persona en la posición actual
        
        # 1. Verificar si alguien se movió más de 2 posiciones adelante (caos)
        if actual - (i + 1) > 2: 
            # la persona deberia estar en la posicion actual-1, 
            print("Too chaotic")
            return
        # 2. Contar cuántos números mayores que 'actual' están delante de 'actual'
        # Revisar desde la posición máxima que puede haber sobornado al actual (max(0, actual-2))
        for j in range(max(0, actual - 2), i):
            if q[j] > actual:
                cont += 1

    print(cont)

    
if __name__ == '__main__':
    q=[2,1,5,3,4]
    #q=[2,5,1,3,4]
    minimumBribes(q)