def jumpingOnClouds(c):
    i = 0  # Start at the first cloud
    cant = 0  # Initialize the jump counter
    tam=len(c)-1
    while i < tam:
        # Check if we can make a jump of 2
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        cant += 1  # Increment the jump counter
    
    return cant

if __name__ == '__main__':
    c = [0, 0, 1, 0, 0, 1, 0]
    print(jumpingOnClouds(c))  # Expected output: 4
