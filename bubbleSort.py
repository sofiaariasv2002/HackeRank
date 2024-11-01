##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (sorting)
# 31 oct 2024
##################################################################################################################

##################################################################################################################
# Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. 
# Once sorted, print the following three lines:

# Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
# First Element: firstElement, where firstElement is the first element in the sorted array.
# Last Element: lastElement, where lastElement is the last element in the sorted array
##################################################################################################################

def countSwaps(a):
    numSwap=0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j]<a[i]:
                aux=a[i]
                a[i]=a[j]
                a[j]=aux
                numSwap+=1

    print("Array is sorted in ",numSwap, " swaps.")
    print("First Element: ", a[0])
    print("Last Element: ", a[len(a)-1])


if __name__ == '__main__':
    a=[4, 2, 3, 1]
    countSwaps(a)