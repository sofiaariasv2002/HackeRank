def hourglassSum(arr):
    suma=0
    result=[]
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            top=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            mid=arr[i+1][j+1]
            bottom=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            suma=top+mid+bottom
            result.append(suma)
            suma=0
    return max(result)

if __name__ == '__main__':
    arr=[[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    print (hourglassSum(arr))