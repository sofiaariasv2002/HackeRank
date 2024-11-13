##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (string)
# 6 nov 2024
##################################################################################################################

##################################################################################################################
# A string is said to be a special string if either of two conditions is met:

# All of the characters are the same, e.g. aaa.
# All characters except the middle one are the same, e.g. aadaa.

# A special substring is any substring of a string which meets one of those criteria. 
# Given a string, determine how many special substrings can be formed from it.
##################################################################################################################

"""
def substrCount(n, s):
    substring=[]
    count=0

    for inicio in range(n):
        for fin in range(inicio+1, n+1):
            substring.append(s[inicio:fin])
    #print(substring)

    for i in substring:
        subdict={}

        for letter in i:
            subdict[letter]=subdict.get(letter,0)+1
        keys=list(set(subdict.keys()))
        values=list(set(subdict.values()))
        if len(keys)==1:
            count+=1
        if len(keys)==2:
            for i in range(len(values)-1):
                if values[i]==1 and values[i+1]==2:
                    count+=1
                if values[i]==2 and values[i+1]==1:
                    count+=1
        
        # print(subdict)
        # print(count)
    #print(subdict)
    return(count)
"""

def substrCount(n, s):
    # Paso 1: Agrupar caracteres consecutivos
    groups = []
    count = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            groups.append((s[i - 1], count))
            count = 1
    groups.append((s[n - 1], count))  # Agregar el último grupo

    # Paso 2: Contar subcadenas especiales
    special_count = 0

    # Contar subcadenas con caracteres consecutivos
    for char, length in groups:
        for i in range(1, length + 1):  # Contar subcadenas acumulando
            special_count += i

    # Contar subcadenas con un carácter diferente en el medio
    for i in range(1, len(groups) - 1):
        if groups[i - 1][0] == groups[i + 1][0] and groups[i][1] == 1:
            # Contar subcadenas especiales que tienen un carácter en medio
            special_count += min(groups[i - 1][1], groups[i + 1][1])

    return special_count

if __name__ == '__main__':
    n=6
    s='aaabba'
    print(substrCount(n, s))