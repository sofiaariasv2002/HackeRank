##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (hash Tables)
# 28 oct 2024
##################################################################################################################

##################################################################################################################
#Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
##################################################################################################################

def sherlockAndAnagrams(s):
    substringDir=dict()
    substring = []
    n = len(s)
    
    # obtener substring
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring.append(s[i:j])  
    print(substring)

    # Ordenar cada subcadena
    for i in range(len(substring)):
        sorted_chars = sorted(substring[i])  
        substring[i] = ''.join(sorted_chars) 
    print(substring)

    # Crear diccionario
    for subs in substring:
        if subs not in substringDir:
            substringDir[subs]=1
        else:
            substringDir[subs]=substringDir[subs]+1
    print(substringDir)

    # Contar pares de anagramas
    cant = 0  
    for value in substringDir.values():  # Iteramos sobre los valores en el diccionario
        if value > 1:  # Solo calculamos pares si el valor es mayor que 1
            pairs = (value * (value - 1)) // 2  # Calculamos el número de pares
            cant += pairs  # Sumamos al total de pares
    return cant




if __name__ == '__main__':
    s="hola"
    print(sherlockAndAnagrams(s))