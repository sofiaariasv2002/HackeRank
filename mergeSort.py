##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (sorting)
# 4 nov 2024
##################################################################################################################

##################################################################################################################
# In an array, arr, the elements at indices i and i (where i<j) form an inversion if arr[i] > arr[j]. 
# In other words, inverted elements arr[i] and arr[j] are considered to be "out of order". To correct an inversion, we can swap adjacent elements.
##################################################################################################################

N_swaps = 0
def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    med = n//2
    sub1 = merge_sort(arr[:med])
    sub2 = merge_sort(arr[med:])

    global N_swaps

    sorted_arr = []
    i, j = 0, 0
    while i < len(sub1) and j < len(sub2):
        if sub1[i] <= sub2[j]:
            sorted_arr.append(sub1[i])
            i += 1
        elif sub1[i] > sub2[j]:
            sorted_arr.append(sub2[j])
            j += 1
            
            N_swaps += len(sub1) - i
    if i < len(sub1):
        sorted_arr += sub1[i:]
        
    if j < len(sub2):
        sorted_arr += sub2[j:]
    return sorted_arr

def countInversions(arr):
    # Write your code here
    global N_swaps
    N_swaps = 0
    merge_sort(arr)
    print (arr)
    return N_swaps

arr=[2, 1, 3, 1, 2]
print(countInversions(arr))