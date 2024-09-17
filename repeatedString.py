def repeatedString(s, n):
    # Contar el número de 'a' en la cadena original
    count_in_s = s.count('a')
    
    # Calcular el número de repeticiones completas de la cadena en el límite n
    full_repeats = n // len(s)
    
    # Contar el número de 'a' en las repeticiones completas
    total_count = full_repeats * count_in_s
    
    # Contar el número de 'a' en la parte restante (si la longitud no es un múltiplo exacto)
    remainder = n % len(s)
    total_count += s[:remainder].count('a')
    
    return total_count

if __name__ == '__main__':
    n=10
    s="abaabca"
    print (repeatedString(s,n))