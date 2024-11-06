##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (sorting)
# 6 nov 2024
##################################################################################################################

##################################################################################################################
# A Shashank le gustan las cadenas donde los caracteres consecutivos son diferentes. 
# Por ejemplo, le gusta ABABA, mientras que ABAA no le gusta. Dada una cadena que solamente contiene 
# caracteres A y B, él quiere cambiarla a una cadena que le guste. 
# Para hacerlo, solo se le permite borrar los caracteres en la cadena.

# Tu tarea es encontrar la mínima cantidad requerida de borrados.
##################################################################################################################

def alternatingCharacters(s):
    delete = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            delete += 1
    return delete


if __name__ == '__main__':
    s='BBBBB'
    print(alternatingCharacters(s))