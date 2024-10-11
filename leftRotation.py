##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit
# 17 sep 2024
##################################################################################################################
##################################################################################################################
# A left rotation operation on an array shifts each of the array's elements  unit to the left. 
# For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].
# Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

# Given an array a of  integers and a number, d, perform  left rotations on the array. 
# Return the updated array to be printed as a single line of space-separated integers."
##################################################################################################################

def rotLeft(a, d):
    cont=0
    while cont < d:
        num=a[0]
        a.append(num)
        a.pop(0)
        cont=cont+1
    return a

if __name__ == '__main__':
    d=4
    a=[1,2,3,4,5,]
    print (rotLeft(a,d))