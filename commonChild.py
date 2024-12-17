##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (strings manipulation)
# 12 nov 2024
##################################################################################################################

##################################################################################################################
# A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from 
# the other string. Letters cannot be rearranged. Given two strings of equal length, what's the longest string 
# that can be constructed such that it is a child of both?
##################################################################################################################

"""""
No funciona ya que busca la subtring mas larga y el problema pide secuencia mas larga

def commonChild(s1, s2):
    s1e=[]
    s2e=[]
    substringS1e=[]
    substringS2e=[]
    resultsubtring=[]
    noe=0
    result=0

    for letter in s1:
        if letter in s2:
            s1e.append(letter)
        else:
            noe+=1
    s1e="".join(s1e)
    print('Letras iguales en s1')
    print(s1e)

    for letter1 in s2:
        if letter1 in s1:
            s2e.append(letter1)
        else:
            noe+=1
    s2e="".join(s2e)
    print('Letras iguales en s2')
    print(s2e)

    if noe==len(s1)+len(s2):
        print (0)

    for i in range (len(s1e)):
        for j in range(i+1,len(s1e)+1):
            substringS1e.append(s1e[i:j])
    print('substrings en s1')
    print(substringS1e)

    for i in range (len(s2e)):
        for j in range(i+1,len(s2e)+1):
            substringS2e.append(s2e[i:j])
    print('substrings en s2')
    print(substringS2e)

    for substring in substringS1e:
        if substring in substringS2e:
            resultsubtring.append(substring)
    print('substrings iguales')
    print(resultsubtring)

    for substring in resultsubtring:
        if len(substring)>result:
            result=len(substring)
    return(result)
"""""

def commonChild(s1, s2):
    # Crear una matriz de DP de tamaño (len(s1) + 1) x (len(s2) + 1)
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Llenar la matriz
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:  # Caracteres coinciden
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Tomar el máximo de excluir un carácter de s1 o s2
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # El valor en dp[len(s1)][len(s2)] es la longitud de la LCS
    return dp[-1][-1]



if __name__ == '__main__':
    s1=''
    s2='SALLY'
    # NHA = 3
    # s1='AA'
    # s2='BB'
    # s1='WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
    # s2='FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'
 
    print(commonChild(s1, s2))