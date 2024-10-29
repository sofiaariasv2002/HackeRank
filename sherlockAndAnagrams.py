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
    

# Ordenar cada subcadena
    for i in range(len(substring)):
        sorted_chars = sorted(substring[i])  # Ordenamos los caracteres
        substring[i] = ''.join(sorted_chars)  # Reconstruimos la cadena ordenada

    return substring


if __name__ == '__main__':
    s="abba"
    print(sherlockAndAnagrams(s))